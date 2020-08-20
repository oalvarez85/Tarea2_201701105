import csv

def leerCSV():
    with open('./Data/data.csv') as File:
        reader = csv.DictReader(File)    
        print('**Se obtuvo un diccionario de el archivo data.csv**')
        print('')
        for row in reader:        
            print('Nombre:', row["Nombre"])
            print('Puesto:', row["Puesto"])
            print('DPI:', row["DPI"])
            print('Edad:', row["Edad"])
            print('')
        print("**La estructura utilizada es:")    
        print(type(reader))
