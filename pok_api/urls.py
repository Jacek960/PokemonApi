from django.urls import path
from pok_api.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view()),
    # path('api/<int:pk>/', DetailPokemon.as_view()),
    # path('api/', ListPokemon.as_view()),
    # path('api/ability/', AbilityPokemon.as_view()),
]
