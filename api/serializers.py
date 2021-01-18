from rest_framework import serializers
from .models import *

#Make serializable class provincia
class ProvinciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Provincia
        fields=['id','province']

#Make serializable class municipio
class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    id_province = serializers.ReadOnlyField(source='id_province.id')
    class Meta:
        model=Municipio
        fields=['id','municipe','id_province']

#Make serializable class bairro
class BairroSerializer(serializers.HyperlinkedModelSerializer):
    id_municipe = serializers.ReadOnlyField(source='id_municipio.id')
    class Meta:
        model=Bairro
        fields=['id','neighbood','street','id_municipe']
