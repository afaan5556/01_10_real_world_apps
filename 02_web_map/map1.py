from geopy.geocoders import ArcGIS
import pandas as pd
from logging import basicConfig
import configparser
import logging
import folium


'''
PSEUDOCODE
Parse config file
Read csv file
Send addresses to nom.geocode to get geocode object and add lat lon to df
Send lat lon and pop up data to folium
Generate and return folium map
'''

def get_addresses_df(full_data_path):
	'''
	Read a local csv file of street address and additional data and return as a dataframe
	full_data_path: The full path to the addresses data
	return: A dataframe of the addresses data
	'''
	addressesDf = pd.read_csv(full_data_path)

	return addressesDf


def add_lat_lon_to_addresses_df(addresses_df):
	'''
	Add the lat and lon data to the addresses dataframe using the ArcGIS library
	addresses_df: The dataframe of the addresses data
	return: The addresses df updated with a full string address, nom objects, and lat lon columns
	'''
	# Set up column with full geocode input address
	addresses_df['geocode_input_address'] = addresses_df['Street'] + ', ' + addresses_df['City'] + ', ' + addresses_df['State/Province'] + ' ' + addresses_df['Code']

	# Set up nom
	nom = ArcGIS()

	# Add nom object for each address as new df column
	addresses_df['nom_object'] = addresses_df['geocode_input_address'].apply(lambda x: nom.geocode(x))

	# Add Lat Lon columns to df
	for i, j in zip(['lat', 'lon'], [0, 1]):
		addresses_df[i] = addresses_df['nom_object'].apply(lambda x: x[1][j])

	return addresses_df


# Create map at SF
def build_folium_map(map_start_lat, map_start_lon, map_start_zoom):
	'''
	Build and return a map with default starting lat lon and zoom values
	using the Folium library
	map_start_lat: Map start latitude
	map_start_lon: Map start longitute
	map_start_zoom: Map start zoom
	return: The base folium map object
	'''
	locationMap = folium.Map(location=[map_start_lat, map_start_lon], zoom_start=map_start_zoom, tiles="Stamen Terrain")

	return locationMap


def add_map_locations_and_data(location_map, addresses_with_lat_lon_df):
	'''
	Add the location markers and pop-up data for each address in the dataframe
	location_map: The base map object returned by the build_folium_map function
	addresses_with_lat_lon_df: The addresses dataframe updated with lot lon columns
	return: The map object with locations added as a feature group
	'''
	# Start a map feature group
	fg = folium.FeatureGroup(name='Locations Map')
	for lat, lon, street, years in zip(list(addresses_with_lat_lon_df['lat']), list(addresses_with_lat_lon_df['lon']), list(addresses_with_lat_lon_df['Street']), list(addresses_with_lat_lon_df['Years'])):
		fg.add_child(folium.Marker(
			location=[lat, lon],
			popup=street + ': ' + years,
			icon=folium.Icon(color='green'))
		)
	location_map.add_child(fg)

	return location_map


def main():
    basicConfig(level=logging.INFO, format="%(asctime)s\t%(levelname)s\t%(message)s")

    # Parsing Config File
    config = configparser.ConfigParser()
    config.read('config.ini')
    DATA_FOLDER_PATH = config['FILE_PATHS']['Data']
    LOCATION_ADDRESSES_FILE_NAME = config['FILE_NAMES']['LocationAddresses']
    MAP_START_LAT = config['CONSTANTS']['MapStartLat']
    MAP_START_LON = config['CONSTANTS']['MapStartLon']
    MAP_START_ZOOM = config['CONSTANTS']['MapStartZoom']
    MAP_FILE_NAME = config['FILE_NAMES']['MapFile']

    # Read csv file
    addressesDf = get_addresses_df(DATA_FOLDER_PATH + LOCATION_ADDRESSES_FILE_NAME)

    # Send addresses to nom.geocode to get geocode object and add lat lon to df
    addressesWithLatLondf = add_lat_lon_to_addresses_df(addressesDf)

    # Build map
    locationMap = build_folium_map(MAP_START_LAT, MAP_START_LON, MAP_START_ZOOM)

    # Add points and pop-up data to map
    locationMap = add_map_locations_and_data(locationMap, addressesWithLatLondf)

    # Save the map out to html
    locationMap.save(DATA_FOLDER_PATH + MAP_FILE_NAME)


if __name__ == '__main__':
    main()
