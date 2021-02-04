from django.urls import path
from restApi.views import ListPokemon, DetailPokemon, AbilityPokemon

urlpatterns = [
    path('<int:pk>/', DetailPokemon.as_view()),
    path('', ListPokemon.as_view()),
    path('ability/', AbilityPokemon.as_view()),
]
