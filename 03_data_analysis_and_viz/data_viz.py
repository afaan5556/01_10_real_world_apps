import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from pytz import utc
import justpy as jp
import numpy as np

# This code from Highcharts Documentation with default attributes
# These are then manipulated with dot notation in this script below

chart_df = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'Data Source: Student Reviews'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.y} on {point.x}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
'''

# Get the data from the csv file
data = pd.read_csv("data/reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()



def app():
	'''
	This function builds the main Quasar page
	return: The quasar page
	'''
	wp = jp.QuasarPage()

	# Add heading and text sections
	h1 = jp.QDiv(a=wp, text="Analysis of Data", classes="text-h3 text-center q-pa-md")
	p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-subtitle1 text-center q-pa-md")

	# Add high-chart components
	hc = jp.HighCharts(a=wp, options=chart_df)
	# Change the default documentation title and data
	hc.options.title.text = "Average Rating by Day"
	hc.options.xAxis.categories = list(day_average.index)
	hc.options.series[0].data = list(day_average['Rating'])


	return wp

# JP has a funny way of calling and serving the page
jp.justpy(app)