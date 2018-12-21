import csv

matrix = []
f = open('/Users/sanghun/PycharmProjects/FirstProject/결과.txt', 'r')
csvReader = csv.reader(f)
for row in csvReader:
    matrix.append(row)

w_count = {}
for matlst in matrix:
    for lst in matlst:
        try: w_count[lst] += 1
        except: w_count[lst]=1
print(w_count)

f.close()