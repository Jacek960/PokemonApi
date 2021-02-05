from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from pok_api.models import Pokemon
from pokemons.forms import PokemonForm, AbilityForm


class PokemonListView(ListView):
    template_name = 'pokemons/list.html'
    model = Pokemon

class PokemonCreateView(LoginRequiredMixin, CreateView):
    form_class = PokemonForm
    template_name = 'pokemons/pokemon_form.html'
    success_url = '/pokemons'


class PokemonDetailsView(View):
    def get(self, request, id):
        pokemon = Pokemon.objects.get(id=id)
        return render(request, 'pokemons/pokemon_details.html', {'pokemon': pokemon})

class PokemonUpdate(LoginRequiredMixin, UpdateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = 'pokemons/pokemon_form.html'
    success_url = '/pokemons'

class PokemonDelete(LoginRequiredMixin, DeleteView):
    model = Pokemon
    template_name = 'pokemons/pokemon_delete.html'
    success_url = '/pokemons/'


class PokemonAbilityCreateView(LoginRequiredMixin, CreateView):
    form_class = AbilityForm
    template_name = 'pokemons/pokemon_form.html'
    success_url = '/pokemons'

