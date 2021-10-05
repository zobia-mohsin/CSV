import matplotlib.pyplot as plt  # to get graph plt name of graph
import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=',')
# delimiter separater how to process the file
# and read it comas separting elements
header_row = next(csv_file)
# tells you different header names, advance to next row and
#  save the previous row in header row variable
print(type(header_row))  # returns a list

# column name and location of header will be given
# tells us where each item is located, max temperature at index 5
for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
# grasp and append max temperatures to list of highs from the csv file
# into the list of highs
for rec in csv_file:
    highs.append(int(rec[5]))  # from file of string to integers

print(highs)


plt.title("Daily High Temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=16)  # no title for x axis
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
# tickmarks on both axis major axis and size 16
plt.plot(highs, c='red')  # create line graph using highs list PLOT


plt.show()
