import csv
exampleFile = open("deniro.csv")
exampleReader = csv.reader(exampleFile)
for row in exampleReader:
    if row[0] < "2001":
        print(', '.join(row))