import csv

with open('data.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:        
        print('Nombre:', row["Nombre"])
        print('Puesto:', row["Puesto"])
        print('DPI:', row["DPI"])
        print('Edad:', row["Edad"])
        print('')