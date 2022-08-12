from django.test import TestCase
from .models import Pokemon, Ability, Type

class URLTests(TestCase):
    def test_testhome(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
class AbilityTestCase(TestCase):
    def test_fields_pokemon_name(self):
        pokemon_test_name = "New Pokemon"
        pokemon = Pokemon(name=pokemon_test_name, height=1, weight=1, health=1, attack=1, defense=1, sprite="www.example.com")
        pokemon.save()
        relationship_test_name = Pokemon.objects.get(name=pokemon_test_name)
        ability = Ability(pokemon_name=relationship_test_name, ability="New Ability")
        ability.save()
        record = Ability.objects.get(id=1)
        self.assertEqual(record.pokemon_name.name, "New Pokemon")

class TypeTestCase(TestCase):
    def test_fields_pokemon_name(self):
        pokemon_test_name = "New Pokemon"
        pokemon = Pokemon(name=pokemon_test_name, height=1, weight=1, health=1, attack=1, defense=1, sprite="www.example.com")
        pokemon.save()
        relationship_test_name = Pokemon.objects.get(name=pokemon_test_name)
        type = Type(pokemon_name=relationship_test_name, type="New Type")
        type.save()
        record = Type.objects.get(id=1)
        self.assertEqual(record.pokemon_name.name, "New Pokemon")
