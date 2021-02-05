from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from pok_api.models import Pokemon
from pokemons.forms import PokemonForm, AbilityForm


class PokemonListView(ListView):
    template_name = 'pokemons/list.html'
    model = Pokemon

class PokemonCreateView(PermissionRequiredMixin, CreateView):
    form_class = PokemonForm
    template_name = 'pokemons/pokemon_form.html'
    success_url = '/pokemons'
    permission_required = 'pok_api.add_pokemon'


class PokemonDetailsView(View):
    def get(self, request, id):
        pokemon = Pokemon.objects.get(id=id)
        return render(request, 'pokemons/pokemon_details.html', {'pokemon': pokemon})

class PokemonUpdate(PermissionRequiredMixin, UpdateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = 'pokemons/pokemon_form.html'
    success_url = '/pokemons'
    permission_required = 'pok_api.change_pokemon'

class PokemonDelete(PermissionRequiredMixin, DeleteView):
    model = Pokemon
    template_name = 'pokemons/pokemon_delete.html'
    success_url = '/pokemons/'
    permission_required = 'pok_api.delete_pokemon'


class PokemonAbilityCreateView(PermissionRequiredMixin, CreateView):
    form_class = AbilityForm
    template_name = 'pokemons/pokemon_form.html'
    success_url = '/pokemons'
    permission_required = 'pok_api.add_ability'

