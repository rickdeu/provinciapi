from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import permissions

#credenciais: user api; password: huilalubango

#make view serializable provincia
class ProvinciaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Provincia.objects.all()
    serializer_class=ProvinciaSerializer

    #permission_classes=[permissions.IsAuthenticated]
#Make view serializable municipio
class MunicipioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Municipio.objects.all()
    serializer_class=MunicipioSerializer
    
#Make view serializable municipio
class BairroViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Bairro.objects.all()
    serializer_class=BairroSerializer
    
