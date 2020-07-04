import csv
with open("file.csv", 'r') as file:
    csvfile = csv.DictReader(file)
    for row in csvfile:
        print(dict(row))