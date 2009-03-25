#!/usr/bin/env python
'''
reads in csv data from file and plots using date as x-index
csv file looks like
2,02/16/09 04:35:00 PM,18.129
3,02/16/09 04:40:00 PM,17.486
4,02/16/09 04:45:00 PM,17.677
5,02/16/09 04:50:00 PM,17.915
'''

import csv
import matplotlib.pyplot as mpl
import datetime
from matplotlib.dates import DateFormatter

fileName = './20090325/1418_Bedroom.csv'
fileHandle = open(fileName)
fileHandle.readline()
fileHandle.readline()
reader = csv.reader(fileHandle)

date = []
temp = []
for row in reader:
    # create a datetime object based on parsing the string
    #thisDate = datetime.datetime.strptime(row[1],'%m/%d/%y %I:%M:%S %p')
    thisDate = datetime.datetime.strptime(row[1],'%y-%m-%d %H:%M:%S ')
    date.append(thisDate)
    temp.append(float(row[2]))

fig = mpl.figure()
ax = fig.add_subplot(111)
# you can pass datetime objects to plot as the x-axis
ax.plot(date,temp)
ax.set_ylabel(r'Temperature ($^\circ$C)')
fig.suptitle('Cottage Indoor Temperature')
# this formats the strings
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M'))
# this rotates the dates so they are readable
fig.autofmt_xdate()
mpl.show()
