from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'manutencoes'

router = routers.DefaultRouter()
router.register('', views.ManutencaoViewSet, basename='manutencoes')

urlpatterns = [
    path('', include(router.urls))
]
