import matplotlib.pyplot as plt  # to get graph plt name of graph
import csv

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=',')

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []

for rec in csv_file:
    highs.append(int(rec[5]))

print(highs)


plt.title("Daily High Temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.plot(highs, c='red')


plt.show()
