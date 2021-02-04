from django.contrib.sites import requests
from django.shortcuts import render, redirect
from .models import Pokemon, Ability
from django.views import View
import requests
from django.db.models import Q


class HomePageView(View):
    def get(self,request):
        return render(request,'pok_api/home.html')


class PokemoniewApi(View):
    def get(self, request):
        books = None
        query = None
        books_list = None
        pokemon_in_data_base = None
        a = []
        pokemon_name = None
        pokemon_image = None
        height = None
        weight = None
        # pok_abilitys = None
        # # books_list = None
        if 'q' in request.GET:
            query = request.GET.get('q')
            pok_req = requests.get(
                f"https://pokeapi.co/api/v2/pokemon/{query}").json()

            # items_amount = len(pok_req)
            # books_list = []

            pokemon_name = pok_req['forms'][0]['name']
            pokemon_image = pok_req['sprites']['other']['official-artwork']['front_default']
            height = pok_req['height']
            weight = pok_req['weight']
            a = []

            for item in range(len(pok_req['abilities'])):
                ability = pok_req['abilities'][item]['ability']['name']
                a.append(ability)

            pokemon_in_data_base = Pokemon.objects.filter(pok_name=query).exists()

        else:
            pok_req = requests.get(
                f"https://pokeapi.co/api/v2/pokemon/?limit=2000").json()['results']

        return render(request, 'pok_api/pok_list.html', {'query': query,
                                                     'pok_req': pok_req,
                                                     'a': a,
                                                     'pokemon_name': pokemon_name,
                                                     'pokemon_image': pokemon_image,
                                                     'height': height,
                                                     'weight': weight,
                                                     'pokemon_in_data_base': pokemon_in_data_base,

                                                     })

    def post(self, request):
        query = request.GET.get('q')
        pok_req = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{query}").json()

        pok_name = pok_req['forms'][0]['name']
        pok_height = pok_req['height']
        pok_weight = pok_req['weight']
        pok_img_url = pok_req['sprites']['other']['official-artwork']['front_default']

        poki = Pokemon.objects.create(
            pok_name=pok_name,
            pok_height=pok_height,
            pok_weight=pok_weight,
            pok_img_url=pok_img_url,
        )
        abilitys = []
        for abilit in range(len(pok_req['abilities'])):
            pok_num, pok_ability = Ability.objects.get_or_create(
                name=pok_req['abilities'][abilit]['ability']['name'])
            abilitys.append(pok_req['abilities'][abilit]['ability']['name'])
            poki.pok_abilitys.add(pok_num)
        print(f'lista {abilitys}')
        return redirect('/api/')
