import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'online_data/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for column_header, column_value in enumerate(header_row):
        print(column_header,column_value)
    dates = []
    min_seaLevel = []
    max_seaLevel = []
    for row in reader:
        try:
            datetimes = datetime.strptime(row[0],'%Y-%m-%d')
            max_level = float(row[10])
            min_level = float(row[12])
        except ValueError:
            print(f"Invalid sea data for {datetimes} found in the file")
        else:
            dates.append(datetimes)
            min_seaLevel.append(min_level)
            max_seaLevel.append(max_level)
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,min_seaLevel,color='blue',alpha = 0.7)
    plt.plot(dates,max_seaLevel,color='red',alpha = 0.7)
    plt.fill_between(dates,max_seaLevel,min_seaLevel,facecolor='black',alpha=0.3)
    plt.xlabel('Date of occurrence',fontsize=10)
    plt.ylabel('sea level',fontsize=10)
    plt.title("Max 'n' min sea level in sitka July, 2014")
    fig.autofmt_xdate()
    #plt.legend()
    plt.savefig("online_data/seaLevel.png", bbox_inches="tight")
    plt.show()

       