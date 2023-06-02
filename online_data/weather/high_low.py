import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'online_data/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    h_temps = []
    l_temps = []
    dates = []
    for row in reader:
        try:
            datetimes = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(f"Missing or Invalid data for {datetimes} found in the dataset")
        else:
            dates.append(datetimes)
            h_temps.append(high)
            l_temps.append(low)
    #print(h_temps)
    fig = plt.figure(dpi=128,figsize=(10,6))
    plt.plot(dates,h_temps,color='red',alpha=0.7)
    plt.plot(dates,l_temps,color='blue',alpha=0.7)
    plt.fill_between(dates,l_temps,h_temps,facecolor='blue',alpha=0.3)
    plt.title("Daily high and  low temperatures-2014 for Dead Valley",fontsize=24)
    plt.xlabel('',fontsize=10)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)',fontsize=10)
    plt.tick_params(axis='both',which='major', labelsize=16)
    #plt.savefig('online_data/deadValleyTemp2014.png',bbox_inches='tight')
    plt.show()