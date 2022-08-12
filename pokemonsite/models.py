from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    health = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sprite = models.URLField(max_length=200)
    def id(self):
        return id(self.id)


class Ability(models.Model):
    pokemon_name = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='ability')
    ability = models.CharField(max_length=100)


class Type(models.Model):
    pokemon_name = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='type')
    type = models.CharField(max_length=100)
    def id(self):
        return id(self.id)




