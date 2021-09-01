# 10 Real World Apps
My code along repo and all associated projects for [this udemy course](https://www.udemy.com/course/the-python-mega-course/)

## 01 English Thesaurus
This project contains 2 versions of a simple english thesaurus:
1. `thesaurus_json_data.py` reads data from a `data/data.json` file to return definitions of user entered words
2. `thesaurus_db_data.py` connects to a `Dictionary` database to return definitions of user entered words

The `thesaurus_json_data.py` version has some additional features such as:
- Finding close but not exact match words
- Prompting the user to confirm if that is what was meant
- Looping through close match options till one is confirmed, or all are exhasted

Both versions handle differences in word capitalization by converting the user input into lowercase

To run directly in shell:
- `python thesaurus_json_data.py`
- `python thesaurus_db_data.py`

## 02 Locations Map Builder
This project builds an interactive map using the Folium library with location pins read from a csv.


It is meant to display the locations where someone has lived, and display the years and total time lived at each location in the popup.


The csv file should have headers as follows:
- street
- city
- state
- country
- code
- years_lived
- total_years_lived


The map generated randomly selects from these availble styles:
- OpenStreetMap
- Stamen Terrain
- Stamen Toner
- CartoDB positron
- CartoDB dark_matter


To run directly in shell:
- Place csv file of locations in `data` folder
- Run `python locations_map_builder.py`


## 03 JustPy Web App
Simple data viz html pages built using the JustPy and HighCharts frameworks.

The Highcharts spline chart type is used, but any other type from the library can be similarly be used as starting JS code and added to a website

#### List Comprehension Tip
Tip for nested list comprehension to inject multipl dataframe series into the HighChart object series attribute:

```
data = [{"name":v1, "data":[v2 for v2 in list(df[v1])]} for v1 in df.columns]
```

## 04 Flask Website
Basic website creation (using Python and Flask) and deployment (Heroku)


## 99 General