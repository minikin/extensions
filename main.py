import numpy as np
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool

x = [0, 100, 1000, 2000, 3000, 5000, 10000]
class_methods = [0, 0.281, 1.7696, 3.5221, 6.3407, 10.4714, 21.0284]
class_extensions = [0, 0.2638, 2.1763, 4.1617, 6.4324, 12.559, 36.4588]
struct_methods = [0, 0.2635, 2.0129, 3.8822, 5.5516, 10.4739, 18.8432]
struct_extensions = [0, 0.2717, 1.7917, 4.0686, 6.406, 13.2296, 32.1629]

yep = 155
firefox_182 = [0.3853]
kickstarter = 280
wire = 381
wordPress = 386

# output to static HTML file
output_file("index.html")

# create a new plot with a title and axis labels
bigPlot = figure(
   tools="pan,box_zoom,reset,save",
   title="Swift: Extensions vs Methods.",
   x_axis_label='number of methods/extensions', 
   y_axis_label='time, s',
   plot_height=180
)

bigPlot.grid.bounds = (0, 2000)

# add a line renderer with legend and line thickness
bigPlot.line(x, class_methods, legend="Class + Methods", line_color="midnightblue", line_width=3)
bigPlot.line(x, class_extensions, legend="Class + Extensions", line_color="orange", line_width=3, line_dash="4 4")
bigPlot.line(x, struct_methods, legend="Struct + Methods", line_color="blue", line_width=3)
bigPlot.line(x, struct_extensions, legend="Struct + Extensions", line_color="orangered", line_width=3, line_dash="12 6")

source = ColumnDataSource(data=dict(
    x=[0, 155, 182, 280, 381, 386],
    y=[0, 0.2011, 0.3853, 0.456, 0.541, 0.555],
    desc=['', 'Yep for iOS', 'Firefox for iOS', 'Kickstarter for iOS', 'Wire for iOS', 'WordPress for iOS'],
    colors = ["white", "darkred", "coral", "darkturquoise", "yellow", "olive"]
))

hover = HoverTool(
    tooltips=[
        ("Extensions", "$x"),
        ("Compilation time", "$y"),
        ("Application", "@desc")],
    # display a tooltip whenever the cursor is vertically in line with a glyph
    mode='vline'
)

smallPlot = figure(
   tools=[hover],
   title="Swift extensions in realword iOS apps",
   x_axis_label='approximate number of extensions', 
   y_axis_label='time, s',
   plot_height=150
)

smallPlot.circle('x', 'y', size=30, source=source, fill_color='colors', line_color='white' )

# show the results
show(column(bigPlot, smallPlot, sizing_mode='scale_width'))