from matplotlib import pyplot as plt
import csv

x = []
y = []

with open('numbers.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,)
plt.xlabel('Price')
plt.ylabel('Date')
plt.title('AirBnB Closing Price')
plt.legend()
plt.show()
