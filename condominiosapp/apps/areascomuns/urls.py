from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'areascomuns'

router = routers.DefaultRouter()
router.register('', views.AreaComumViewSet, basename='areascomuns')

urlpatterns = [
    path('', include(router.urls))
]
