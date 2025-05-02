from datetime import date
import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7fe719c3f4780bb752c505e4fd1e947d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '37456'


def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'Сменил имя'

    

def test_treiner_name():
    response_get = requests.get(url = f'{URL}/trainers/37456', headers=HEADER)
    assert response_get.json()['trainer_name'] == 'Max'


