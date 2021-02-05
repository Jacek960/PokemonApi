from django.contrib import admin

# Register your models here.
from pok_api.models import Pokemon, Ability

admin.site.register(Pokemon)
admin.site.register(Ability)
