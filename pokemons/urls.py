from django.urls import path
from pokemons.views import PokemonListView, PokemonUpdate, PokemonDetailsView, PokemonDelete, PokemonCreateView

urlpatterns = [
    path('', PokemonListView.as_view(), name='pokemon_list'),
    path('<int:id>/', PokemonDetailsView.as_view(),name='pokemon_details'),
    path('update/<int:pk>/',PokemonUpdate.as_view(), name='pokemon_update'),
    path('delete/<int:pk>/',PokemonDelete.as_view(), name='pokemon_delete'),
    path('add/',PokemonCreateView.as_view(), name='pokemon_add'),
]
