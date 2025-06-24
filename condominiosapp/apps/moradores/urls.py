from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'moradores'

router = routers.DefaultRouter()
router.register('', views.MoradorViewSet, basename='moradores')

urlpatterns = [
    path('', include(router.urls))
]
