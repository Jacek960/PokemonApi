from django.shortcuts import render
from pok_api.models import Pokemon, Ability
from .serializers import PokemonSerializer, AbilitySerializer
from rest_framework import generics


# Django REST framework Views

class ListPokemon(generics.ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class DetailPokemon(generics.RetrieveAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class AbilityPokemon(generics.ListAPIView):
    queryset = Ability.objects.all()
    serializer_class = AbilitySerializer
