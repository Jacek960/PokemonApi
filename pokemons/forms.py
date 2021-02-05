from django import forms
from pok_api.models import Pokemon, Ability


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['pok_name',
                  'pok_height',
                  'pok_weight',
                  'pok_img_url',
                  'pok_abilitys',
                  ]

class AbilityForm(forms.ModelForm):
    class Meta:
        model = Ability
        fields = ['name',
                  ]

