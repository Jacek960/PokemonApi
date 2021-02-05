from django.urls import path
from pok_api.views import HomePageView, PokemoniewApi

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/', PokemoniewApi.as_view(), name='pokemon_api'),
]
