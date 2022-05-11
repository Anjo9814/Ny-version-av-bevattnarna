import pygal
from FINALdatabase_management import \
    time_log_for_svg, temp_log_for_svg, retrieve_data

dates_final = time_log_for_svg(retrieve_data())
temperatures = temp_log_for_svg(retrieve_data())
date_chart = pygal.Line(range=(17, 25), dots_size=5,
                        show_y_guides=False, x_label_rotation=20)
date_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), dates_final)
date_chart.add("Temperature", temperatures)
date_chart_data = date_chart.render_to_file('Pleasework.svg')
