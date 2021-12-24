import math
import csv

with open('data.csv', newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)

data = filedata[0]
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return(mean)

list = []
for number in data:
    a = int(number) - mean(data)
    a = a ** 2
    list.append(a)

sum = 0
for i in list:
    sum = sum+i 
result = sum/(len(data)-1)
standarddeviation = math.sqrt(result)
print(standarddeviation)