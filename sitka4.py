import matplotlib.pyplot as plt  # to get graph plt name of graph
import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=',')

header_row = next(csv_file)

# print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
lows = []
# testing the datetime strptime function
mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
# print(mydate)
# print(type(mydate))  # to convert test to date use datetime

for rec in csv_file:

    try:
        the_date = datetime.strptime(rec[2], '%Y-%m-%d')
        high = int(rec[4])  # to account for the missing data in line 50
        low = int(rec[5])  # changed the index based on death valley file

    except ValueError:  # only print this if error with data
        # variable name in the string literal with the curly brackets
        print(f'Missing data for {the_date}')
    else:
        highs.append(high)
        lows.append(low)
        dates.append(the_date)

    # highs.append(int(rec[4]))
    # lows.append(int(rec[5]))
    #the_date = datetime.strptime(rec[2], '%Y-%m-%d')
    # dates.append(the_date)


# print(highs)
# print(dates)


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
# if you want one figure with two graphs, number of rows, number of columns, which one are you talking about
# the graph, 1 or 2

# HOMEWORK for sitca and deathvalley, look at file and see how it is made up, specially look at index values
# do automatic index value, get it based on files
plt.subplot(2, 1, 1)
plt.plot(dates, highs, c='red')
plt.title("Highs")


plt.subplot(2, 1, 2)
plt.plot(dates, lows, c='blue')
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show()
