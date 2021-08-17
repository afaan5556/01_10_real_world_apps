import folium

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

