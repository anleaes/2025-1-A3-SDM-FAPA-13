from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'reservas'

router = routers.DefaultRouter()
router.register('', views.ReservaAreaComumViewSet, basename='reservas')

urlpatterns = [
    path('', include(router.urls))
]