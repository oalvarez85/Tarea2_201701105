import json

with open('data.json') as file:
    data = json.load(file)
    for client in data['personas']:
        print('Nombre:', client['nombre'])
        print('Apellido:', client['apellido'])
        print('Sexo:', client['sexo'])
        print('Edad:', client['edad'])
        print('')