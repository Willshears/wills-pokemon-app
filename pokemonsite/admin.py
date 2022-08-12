from django.contrib import admin

from .models import Pokemon
from .models import Ability
from .models import Type
admin.site.register(Pokemon)
admin.site.register(Ability)
admin.site.register(Type)