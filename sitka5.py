import matplotlib.pyplot as plt  # to get graph plt name of graph
import csv
from datetime import datetime

# Throughout file 1 will be death valley and all components
# of file 2 wil be sitka, all codes done twice.

open_file1 = open("death_valley_2018_simple.csv", "r")
open_file2 = open('sitka_weather_2018_simple.csv', 'r')

csv_file1 = csv.reader(open_file1, delimiter=',')
csv_file2 = csv.reader(open_file2, delimiter=',')


header_row1 = next(csv_file1)
header_row2 = next(csv_file2)


# print(type(header_row))

for index, column_header in enumerate(header_row1):
    print(index, column_header)
for index, column_header in enumerate(header_row2):
    print(index, column_header)

highs = []
dates = []
lows = []
highs2 = []
dates2 = []
lows2 = []
# testing the datetime strptime function
#mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
# print(mydate)
# print(type(mydate))  # to convert test to date use datetime

for rec in csv_file1:

    try:
        the_date = datetime.strptime(rec[2], '%Y-%m-%d')
        high = int(rec[4])  # to account for the missing data in line 50
        low = int(rec[5])  # changed the index based on death valley file

    except ValueError:  # only print this if error with data
        # variable name in the string literal with the curly brackets
        print(f'Missing data for {the_date}')  # f string, avoids commas
    else:
        highs.append(high)
        lows.append(low)
        dates.append(the_date)


# HOW DO I AVOID HARDCODING THE INDEX VALUES??

for rec in csv_file2:

    try:
        the_date = datetime.strptime(rec[2], '%Y-%m-%d')
        high = int(rec[5])  # to account for the missing data in line 50
        low = int(rec[6])  # changed the index based on death valley file

    except ValueError:  # only print this if error with data
        # variable name in the string literal with the curly brackets
        print(f'Missing data for {the_date}')  # f string, avoids commas
    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(the_date)

    # highs.append(int(rec[4]))
    # lows.append(int(rec[5]))
    #the_date = datetime.strptime(rec[2], '%Y-%m-%d')
    # dates.append(the_date)


# print(highs)
# print(dates)

'''
fig = plt.figure()
plt.title("Daily High and Low Temperatures -2018\nDeath Valley", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='both', labelsize=12)
fig.autofmt_xdate()  # auto format the dates axis which has dates

plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.show()
'''
# if you want one figure with two graphs, number of rows, number of columns, which one are you talking about
# the graph, 1 or 2

# HOMEWORK for sitca and deathvalley, look at file and see how it is made up, specially look at index values
# do automatic index value, get it based on files
fig = plt.figure()
plt.subplot(2, 1, 2)  # two rows, one column, top graph
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.title("DEATH VALLEY, CA US")
plt.xlabel("", fontsize=10)
plt.ylabel("Temperature (F)", fontsize=10)
plt.ylim(10, 140)
plt.tick_params(axis='both', which='both', labelsize=10)
fig.autofmt_xdate()
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.subplot(2, 1, 1)
plt.plot(dates2, highs2, c='red', alpha=0.5)
plt.plot(dates2, lows2, c='blue', alpha=0.5)
plt.title("SITKA AIRPOT, AK US")
plt.xlabel("", fontsize=10)
plt.ylabel("Temperature (F)", fontsize=10)
plt.ylim(10, 80)
plt.tick_params(axis='both', which='both', labelsize=10)
fig.autofmt_xdate()
plt.suptitle(
    "Temperature Comparison between SITCA AIRPORT, AK US and DEATH VALLEY, CA US", fontsize=10)
plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)

plt.show()
