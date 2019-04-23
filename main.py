import numpy as np
from bokeh.io import output_file, show
from bokeh.layouts import column
from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import HoverTool

# Data for plot a
x = [0, 100, 1000, 2000, 3000, 5000, 10000]
class_methods = [0, 0.31, 2.011, 4.011, 6.036, 10.062, 20.22]
class_extensions = [0, 0.314, 2.117, 4.493, 7.171, 13.209, 32.147]
struct_methods = [0, 0.304, 1.953, 3.864, 5.84, 9.734, 19.583]
struct_extensions = [0, 0.312, 2.18, 4.5, 7.114, 13.141, 31.756]

# class_methods_private = [0, 0.677, 1.7158, 3.4679, 5.2614, 9.7713, 19.562]
# class_extensions_private = [0, 0.1874, 1.175, 2.7621, 4.2379, 8.411, 25.3922]

# Data for plot b
x_apps = [0, 46, 144, 155, 182, 280, 381, 388]
apps_extensions = [0, 0.209, 0.386, 0.407, 0.455, 0.639, 0.832, 0.847]
apps_methods = [0, 0.208, 0.381, 0.422, 0.457, 0.632, 0.824, 0.854]

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
# plot_a.line(x, class_methods_private, legend='Class + Private Methods', line_color='teal', line_width=2)
# plot_a.line(x, class_extensions_private, legend='Class + Private Functions', line_color='cyan', line_width=3, line_dash='5 12')

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
