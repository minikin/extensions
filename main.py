import numpy as np
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool

# Data for plot a
x = [0, 100, 1000, 2000, 3000, 5000, 10000]
class_methods = [0, 0.3757, 2.1785, 4.2088, 6.3451, 10.4275, 21.1682]
class_extensions = [0, 0.3756, 2.3054, 4.8083, 7.6901, 14.1323, 34.7975]
struct_methods = [0, 0.3647, 2.1105, 4.0591, 5.9957, 10.1222, 20.5082]
struct_extensions = [0, 0.3642, 2.2164, 4.9483, 7.2034, 13.2632, 33.7204]

# Data for plot b
x_apps = [0, 46, 144, 155, 182, 280, 381, 388]
apps_extensions = [0, 0.2602, 0.4401, 0.4611, 0.5453, 0.7477, 0.943, 0.9441]
apps_methods = [0, 0.2728, 0.455, 0.4608, 0.5115, 0.7121, 0.9154, 0.9003]

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
plot_a.line(x, class_methods, legend='Class + Methods',
            line_color='midnightblue', line_width=2)
plot_a.line(x, class_extensions, legend='Class + Extensions',
            line_color='orange', line_width=3, line_dash='4 4')
plot_a.line(x, struct_methods, legend='Struct + Methods',
            line_color='blue', line_width=3)
plot_a.line(x, struct_extensions, legend='Struct + Extensions',
            line_color='orangered', line_width=2, line_dash='12 6')

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
    colors=['white',
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
    title='Swift extensions in real world apps',
    x_axis_label='approximate number of extensions in apps',
    y_axis_label='compilation time, s',
    plot_height=150
)

circle = plot_b.circle('x', 'y', size=25, source=sourceForPlotB,
                       fill_color='colors', line_color='white')
plot_b.line(x_apps, apps_extensions, legend="Struct + Extensions",
            line_color="red", line_width=2)
plot_b.line(x_apps, apps_methods, legend="Class + Methods",
            line_color="blue", line_width=2, line_dash="4 4")
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
