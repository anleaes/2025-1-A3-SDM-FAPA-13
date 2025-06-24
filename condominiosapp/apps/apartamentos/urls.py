from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'apartamentos'

router = routers.DefaultRouter()
router.register('', views.ApartamentoViewSet, basename='apartamentos')

urlpatterns = [
    path('', include(router.urls))
]