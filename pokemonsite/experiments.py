import requests
import json

def main():
    # ## we define a request object that is equal to requests.get('API')
    # all_pokemon_call = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10000')
    # all_pokemon_response = json.loads(all_pokemon_call.content)
    # print(all_pokemon_call.status_code)
    # pokemon_count = all_pokemon_response['results']
    # pokemon_urls = [item.get('url') for item in pokemon_count]
    # for url in pokemon_urls:
    #     single_pokemon_call = requests.get(url)
    #     single_pokemon_response = json.loads(single_pokemon_call.content)
    #     name = single_pokemon_response['species']['name']
    #     height = single_pokemon_response['height']
    #     weight = single_pokemon_response['weight']
    #     sprite = single_pokemon_response['sprites']['front_default']
    #     health = single_pokemon_response['stats'][0]['base_stat']
    #
    #     for ability in single_pokemon_response['abilities']:
    #         ability_names = ability['ability']['name']
    #     for type in single_pokemon_response['types']:
    #         type_names = type['type']['name']
    single_pokemon_call = requests.get('https://pokeapi.co/api/v2/pokemon/wyrdeer')
    single_pokemon_response = json.loads(single_pokemon_call.content)
    sprite = single_pokemon_response['sprites']['front_default']
    print(sprite)

if __name__ == '__main__':
    main()