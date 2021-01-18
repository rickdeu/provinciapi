from rest_framework import serializers
from .models import *

#Make serializable class provincia
class ProvinciaSerializer(serializers.HyperlinkedModelSerializer):
    #id_provincia = serializers.HyperlinkedRelatedField(many=True, view_name='provincia-detail', read_only=True)

    class Meta:
        model=Provincia
        fields=['id','province']

#Make serializable class municipio
class MunicipioSerializer(serializers.HyperlinkedModelSerializer):
    #provincia = serializers.ReadOnlyField(source='id_provincia.provincia')
    id_province = serializers.ReadOnlyField(source='id_province.id')


    class Meta:
        model=Municipio
        fields=['id','municipe','id_province']

#Make serializable class bairro
class BairroSerializer(serializers.HyperlinkedModelSerializer):
    #municipio = serializers.ReadOnlyField(source='id_municipio.municipio')
    id_municipe = serializers.ReadOnlyField(source='id_municipio.id')
    class Meta:
        model=Bairro
        fields=['id','neighbood','street','id_municipe']