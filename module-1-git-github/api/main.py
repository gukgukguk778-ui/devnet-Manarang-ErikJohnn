import requests


pokemon1 = requests.get('https://pokeapi.co/api/v2/pokemon/beedrill')
pokemon2 = requests.get('https://pokeapi.co/api/v2/pokemon/parasect')
pokemon3 = requests.get('https://pokeapi.co/api/v2/pokemon/onix')
pokemon4 = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
pokemon5 = requests.get('https://pokeapi.co/api/v2/pokemon/wooper')

name1 = pokemon1.json()['name']
height1 = pokemon1.json()['height']
weight1 = pokemon1.json()['weight']

name2 = pokemon2.json()['name']
height2 = pokemon2.json()['height']
weight2 = pokemon2.json()['weight']

name3 = pokemon3.json()['name']
height3 = pokemon3.json()['height']
weight3 = pokemon3.json()['weight']

name4 = pokemon4.json()['name']
height4 = pokemon4.json()['height']
weight4 = pokemon4.json()['weight']

name5 = pokemon5.json()['name']
height5 = pokemon5.json()['height']
weight5 = pokemon5.json()['weight']


print(response.content)
