import csv

with open("deniro.csv") as csvdatei:
    csv_reader_object = csv.reader(csvdatei)
    for row in csv_reader_object:
        print(', '.join(row))



import csv

with open("deniro.csv") as csvdatei:
    csv_reader_object = csv.reader(csvdatei)

    zeilennummer = 0
    for row in csv_reader_object:

        if zeilennummer == 0:
            print(f'Spaltennamen sind: {", ".join(row)}')
        else:
            print(f'- Year: {row[0]} \t| Score: {row[1]} \t| Title: {row[2]}.')
        zeilennummer += 1

    print(f'Anzahl Datensätze: {zeilennummer-1}')