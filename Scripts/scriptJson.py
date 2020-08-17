import json

def leerJson():
    with open("./Data/data.json") as file:
        data = json.load(file)
        print('**Se obtuvo un diccionario de el archivo data.json**')
        print('')
        for client in data['personas']:
            print('Nombre:', client['nombre'])
            print('Apellido:', client['apellido'])
            print('Sexo:', client['sexo'])
            print('Edad:', client['edad'])
            print('')