import csv

with open("deniro.csv") as csvdatei:
    csv_reader_object = csv.reader(csvdatei)

    zeilennummer = 0
    for row in csv_reader_object:
        print(row[0])