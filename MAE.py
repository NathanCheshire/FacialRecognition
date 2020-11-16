#I used this file to calculate the MAE value between two columns of integers
#5,6
#3,2
#would produce a MAE of 1

import csv
FILE = "MAE_RAW.txt"

#mean absolute error = (Sum from i=1 to i=n of (abs(yi - xi))) / n
#where x or y is the truth and the other is the result you received

#open file
f = open(FILE, 'r')

#init for loop vars
lines = f.readlines()
numLines = len(lines)
acc = 0;

#compute sum of MAEs
for line in lines:
    parts = line.split(',')
    acc += abs((int(parts[0])) - (int(parts[1])))

#get average MAE
acc /= numLines   

#inform of MAE
print('MAE for ' + FILE + " is: " + str(acc))