from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'eventos'

router = routers.DefaultRouter()
router.register('', views.EventoViewSet, basename='eventos')

urlpatterns = [
    path('', include(router.urls))
]
