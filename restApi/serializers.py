from rest_framework import serializers
from pok_api.models import Pokemon, Ability


class AbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Ability
        fields = ('id', 'name',)


class PokemonSerializer(serializers.ModelSerializer):
    pok_abilitys = AbilitySerializer(read_only=True, many=True)

    class Meta:
        model = Pokemon
        fields = ('id', 'pok_name', 'pok_height',
                  'pok_weight', 'pok_img_url', 'pok_abilitys')
