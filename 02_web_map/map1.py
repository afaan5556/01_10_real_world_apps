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
Send addresses to nom.geocode to get geocode object
Parse geocode object to get lat lon and pop up data
Send lat lon to and pop up data to folium
Generate and return folium map
'''

# Recipe for getting lat lon from an address
nom = ArcGIS()
nom.geocode("8 Colonial Way, San Francisco, CA 94112")


# Create map at SF
map1 = folium.Map(location=[37.768230196198026, -122.42936027298293], zoom_start=13, tiles="Stamen Terrain")

# Add markers without feature group
# map1.add_child(folium.Marker(
# 	location=[37.768230196198026, -122.42936027298293],
# 	popup="Church Street Pad",
# 	icon=folium.Icon(color='green'))
# )

# Add features as part of group
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(
	location=[37.768230196198026, -122.42936027298293],
	popup="Church Street Pad",
	icon=folium.Icon(color='green'))
)

map1.add_child(fg)


# Save map
map1.save("Map1.html")

def get_addresses(full_data_path):
	'''
	full_data_path: The full path to the addresses data
	return: A dataframe of the addresses data
	'''
	addressesDf = pd.read_csv(full_data_path)

	return addressesDf


def get_geocode_object_list(addresses_df):
	'''
	addresses_df: The dataframe of the addresses data
	return: A list of geocode objects for each row in the addresses data dataframe
	'''


def main():
    basicConfig(level=logging.INFO, format="%(asctime)s\t%(levelname)s\t%(message)s")

    # Parsing Config File
    config = configparser.ConfigParser()
    config.read('config.ini')
    DATA_FOLDER_PATH = config['FILE_PATHS']['Data']
    LOCATION_ADDRESSES_FILE_NAME = config['FILE_NAMES']['LocationAddresses.csv']

    # Read csv file
    addressesDf = get_addresses(DATA_FOLDER_PATH + LOCATION_ADDRESSES_FILE_NAME)

    # Send addresses to nom.geocode to get geocode object
    geoCodeObjects = get_geocode_object_list(addressesDf)



if __name__ == '__main__':
    main()