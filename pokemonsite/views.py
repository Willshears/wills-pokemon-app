from django.shortcuts import render
from .models import Pokemon
from .models import Ability
from .models import Type
import requests
import json

def scraper():
    # Returns an index of all the Pokemon
    all_pokemon_call = requests.get('https://pokeapi.co/api/v2/pokemon?limit=10000')
    if all_pokemon_call:
        all_pokemon_response = json.loads(all_pokemon_call.content)
        pokemon_count = all_pokemon_response['results']
        # To scrape the data, pokemon_urls returns all of the URLs found within the index.
        pokemon_urls = [item.get('url') for item in pokemon_count]
        for url in pokemon_urls:
            single_pokemon_call = requests.get(url)
            if single_pokemon_call:
                single_pokemon_response = json.loads(single_pokemon_call.content)
                pokemon_name = single_pokemon_response['species']['name']
                height = single_pokemon_response['height']
                weight = single_pokemon_response['weight']
                health = single_pokemon_response['stats'][0]['base_stat']
                attack = single_pokemon_response['stats'][1]['base_stat']
                defense = single_pokemon_response['stats'][2]['base_stat']
                sprite = single_pokemon_response['sprites']['front_default']
                # The pokemon are either updated or created, one by one. This is not very effective when running in dev mode synchronously, but it will work
                # if we later wanted to run live updates on the tables. Otherwise, a bulk create and update may be more optimal.
                if sprite == None:
                    sprite = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png'
                add_pokemon, __ = Pokemon.objects.get_or_create(
                    name=pokemon_name,
                    height = height,
                    weight = weight,
                    health = health,
                    attack=attack,
                    defense=defense,
                    sprite=sprite,
                )
                add_pokemon.save()
                try:
                    current_relation = Pokemon.objects.get(name=pokemon_name)
                except:
                    current_relation = Pokemon.objects.filter(name=pokemon_name)[0]
                for ability in single_pokemon_response['abilities']:
                    ability_names = ability['ability']['name']
                    add_ability, __ = Ability.objects.get_or_create(
                        pokemon_name=current_relation,
                        ability=ability_names
                    )
                    add_ability.save()
                for type in single_pokemon_response['types']:
                    type_names = type['type']['name']
                    add_type, __ = Type.objects.get_or_create(
                        pokemon_name=current_relation,
                        type=type_names
                    )
                    add_type.save()


def home(request):
    characters = Pokemon.objects.all().prefetch_related('ability', 'type')
    abilities = Ability.objects.all()
    types = Type.objects.all()
    context = {
        'characters': characters,
        'abilities': abilities,
        'types': types
    }
    if request.method == 'POST':
        scraper()
    return render(request, 'pokemonsite/home.html', context)



