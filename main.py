import numpy as np
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool

# Data for plot a
x = [0, 100, 1000, 2000, 3000, 5000, 10000]
class_methods = [0, 0.281, 1.7696, 3.5221, 6.3407, 10.4714, 21.0284]
class_extensions = [0, 0.2638, 2.1763, 4.1617, 6.4324, 12.559, 36.4588]
struct_methods = [0, 0.2635, 2.0129, 3.8822, 5.5516, 10.4739, 18.8432]
struct_extensions = [0, 0.2717, 1.7917, 4.0686, 6.406, 13.2296, 32.1629]

# Data for plot b
x_apps = [0, 46, 144, 155, 182, 280, 381, 388]
apps_extensions = [0, 0.1699, 0.3513, 0.3532, 0.4463, 0.5542, 0.711, 0.7217]
apps_methods = [0, 0.1686, 0.3258, 0.3704, 0.5273, 0.5744, 0.6992, 0.7124]

# output to static HTML file
output_file("index.html")

# create a new plot with a title and axis labels
plot_a = figure(
   tools='pan,box_zoom,reset,save',
   title='Benchmark of Swift extensions vs methods',
   x_axis_label='number of methods/extensions', 
   y_axis_label='compilation time, s',
   plot_height=180
)

plot_a.grid.bounds = (0, 2000)

# add a line renderer with legend and line thickness
plot_a.line(x, class_methods, legend='Class + Methods', line_color='midnightblue', line_width=3)
plot_a.line(x, class_extensions, legend='Class + Extensions', line_color='orange', line_width=3, line_dash='4 4')
plot_a.line(x, struct_methods, legend='Struct + Methods', line_color='blue', line_width=3)
plot_a.line(x, struct_extensions, legend='Struct + Extensions', line_color='orangered', line_width=3, line_dash='12 6')
plot_a.legend.location = 'top_left'

sourceForPlotB = ColumnDataSource(data=dict(
    x=x_apps,
    y=apps_extensions,
    desc=['', 
        'The Artsy Auction Kiosk App', 
        'CotEditor for macOS', 
        'Yep for iOS', 
        'Firefox for iOS', 
        'Kickstarter for iOS', 
        'Wire for iOS', 
        'WordPress for iOS'],
    colors = ['white', 
        'orangered',
        'coral', 
        'darkturquoise', 
        'lawngreen', 
        'green',
        'dodgerblue',
        'deeppink']
))

plot_b = figure(
    tools='save',
    title='Swift extensions in realword apps',
    x_axis_label='approximate number of extensions in apps', 
    y_axis_label='compilation time, s',
    plot_height=150
)

circle = plot_b.circle('x', 'y', size=25, source=sourceForPlotB, fill_color='colors', line_color='white')
plot_b.line(x_apps, apps_methods, legend="Class + Methods", line_color="blue", line_width=2, line_dash="4 4")
plot_b.legend.location = 'top_left'

hover = HoverTool(
    tooltips=[
        ('Application', '@desc'),
        ("Extensions", '@x{0}'),
        ('Compilation time', '$y')],
    # display a tooltip whenever the cursor is vertically in line with a glyph
    mode='vline',
    renderers=[circle]
)
plot_b.add_tools(hover)

# show the results
show(column(plot_a, plot_b, sizing_mode='scale_width'))