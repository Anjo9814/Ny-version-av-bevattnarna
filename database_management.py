import sqlite3
from datetime import datetime
from csv_to_database import data_converter

conn = sqlite3.connect('temperature_test1.db')
c = conn.cursor()

# c.execute("""CREATE TABLE temperatures (
#             temperature float,
#             time text
#             )""")


def insert_data():
    with conn:
        for rows in data_converter():
            c.execute("INSERT INTO temperatures VALUES (:temperature, :time)",
                      {'temperature': rows[0],
                       'time': rows[1]})

def retrieve_data():
    c.execute("SELECT * FROM temperatures")
    all_values = c.fetchall()
    return all_values

def time_log_for_svg(database):
    # Pull the Time values from the file
    dates = []
    for row in database:
        date = []
        try:
            # Collect the digits for each section of the date
            day = int(row[1][:2])
            month = int(row[1][3:5])
            # Add 2000 to get the year (e.g., 22 -> 2022)
            year = int(row[1][6:8]) + 2000
        except ValueError:
            print('Something went wrong.')
        else:
            # Reconstruct the specific dates
            date.append(year)
            date.append(month)
            date.append(day)
            # Add the dates to the list of all dates
            dates.append(date)


# Construct the list to pass in the lambda function for the plot
    dates_final = []
    for specific_dates in dates:
        elements = datetime(specific_dates[0], specific_dates[1], specific_dates[2])
        dates_final.append(elements)
    return dates_final


def temp_log_for_svg(database):
    temperatures = []
    for row in database:
        temperatures.append(row[0])
    return temperatures

