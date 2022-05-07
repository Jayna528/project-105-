
import math



# list of elements to calculate mean
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]
data1 = []

# finding mean
def mean(data):
    n= len(data)
    total =0
    for x in data:
        total += int(x)

    mean = total / n
    return mean
 

for x in data:
    a = int(x) - mean(data)
    a = a**2
    data1.append(a)

total1 = 0
for x in data1:
    total1 += int(x)


result = total1/(len(data)-1)

SD = math.sqrt(result)

print('The standard Deviation is:', SD)
