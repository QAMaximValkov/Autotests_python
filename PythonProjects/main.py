import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7fe719c3f4780bb752c505e4fd1e947d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_registrarion = {
    "trainer_token": TOKEN,
    "email": "maximusvalkovus2@gmail.com",
    "password": "Iloveqa1111"
}
body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Шпиониро Голубиро",
    "photo_id": 25
}

body_rename = {
    "pokemon_id": "306557",
    "name": "Сменил имя",
    "photo_id": 3
}

body_add_pokeball = {
    "pokemon_id": "306550"
}



'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registrarion)
print(response.text)'''


'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registrarion)
print(response_confirmation.text)'''



'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) 
print(response_create.text)

message = response_create.json()['message']
print(message)'''


'''response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)

message = response_rename.json()['message']
print(message)'''



response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

message = response_add_pokeball.json()['message']
print(message)
