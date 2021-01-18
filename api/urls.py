from rest_framework.routers import DefaultRouter
from api import views
from django.urls import path, include

router=DefaultRouter()
router.register(r'provincia', views.ProvinciaViewSet)
router.register(r'municipio', views.MunicipioViewSet)
router.register(r'bairro', views.BairroViewSet)


urlpatterns=[
    path('', include(router.urls)),
]