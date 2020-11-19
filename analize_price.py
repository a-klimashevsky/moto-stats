import pandas as pd
import matplotlib.pyplot as plt
from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show , ColumnDataSource
from bokeh.models.ranges import DataRange1d
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

path = os.path.join(__location__, "auto_ru_yamaha.csv")


titanic = pd.read_csv(path)


glides = titanic[lambda x: x["model"] == "YZF_R6"]

means = glides.groupby(["year"]).mean()
diff = means.pct_change() * 100
count = glides.groupby(["year"]).count()

print(count)
p1 = figure(title="Yamaha YZF-R6", plot_height=350)
p1.grid.grid_line_alpha=0.3
p1.xaxis.axis_label = 'Year'
p1.yaxis.axis_label = 'Price'
p1.x_range = DataRange1d(start = 2021, end = 1995)
p1.line(source = ColumnDataSource(means), x='year', y='price', color='#A6CEE3')

p2 = figure(title = "Yamaha YZF-R6", plot_height=150)
p2.xaxis.axis_label = 'Year'
p2.yaxis.axis_label = 'Count'
p2.vbar(source = ColumnDataSource(count),x = 'year', top='price', width=0.9)
p2.x_range = DataRange1d(start = 2021, end = 1995)

p3 = figure(title = "Yamaha YZF-R6", plot_height=150)
p3.xaxis.axis_label = 'Year'
p3.yaxis.axis_label = 'Loose'
p3.vbar(source = ColumnDataSource(diff),x = 'year', top='price', width=0.9)
p3.x_range = DataRange1d(start = 2021, end = 1995)

show(gridplot([[p1,None],[p2, None],[p3,None]]))
