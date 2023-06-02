import csv
from datetime import datetime
from matplotlib import pyplot as plt

filenames = ['online_data/death_valley_2014.csv', 'online_data/sitka_weather_2014.csv']
header_rows = {}
h_temps = {}
l_temps = {}
dates = {}

for filename in range(len(filenames)):
    with open(filenames[filename]) as f:
        reader = csv.reader(f)
        header_rows[filename] = next(reader)
        for row in reader:
            try:
                datetimes = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(f"Missing or Invalid data {high} for {datetimes} found in the dataset")
            else:
                if filename in dates:
                    dates[filename].append(datetimes)
                    h_temps[filename].append(high)
                    l_temps[filename].append(low)
                else:
                    dates[filename] = [datetimes]
                    h_temps[filename] = [high]
                    l_temps[filename] = [low]

for key, values in h_temps.items():
    plt.plot(values,label=key)
for key, values in l_temps.items():
    plt.plot(values,label=key)
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Values of Lists in Dictionary')
plt.legend()
plt.show()