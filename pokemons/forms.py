from django import forms
from pok_api.models import Pokemon


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['pok_name',
                  'pok_height',
                  'pok_weight',
                  'pok_img_url',
                  'pok_abilitys',
                  ]
