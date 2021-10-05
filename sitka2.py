import matplotlib.pyplot as plt  # to get graph plt name of graph
import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=',')

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
# testing to convert date from string
mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')  # specify formart
print(mydate)
print(type(mydate))  # to convert test to date use datetime

for rec in csv_file:
    highs.append(int(rec[5]))
    the_date = datetime.strptime(rec[2], '%Y-%m-%d')
    dates.append(the_date)

for rec in csv_file:
    highs.append(int(rec[5]))

print(highs)
print(dates)

fig = plt.figure()


plt.title("Daily High Temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='both', labelsize=12)
fig.autofmt_xdate()  # auto format the dates axis which has dates

plt.plot(dates, highs, c='red')


plt.show()
