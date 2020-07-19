from rest_framework import serializers
from .models import Endereco

class EnderecoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Endereco
        fields = (
            'id',
            'url',
            'streetName',
            'number',
            'complement',
            'neighbourhood',
            'city',
            'state',
            'country',
            'zipcode',
            'latitude',
            'longitude'
        )