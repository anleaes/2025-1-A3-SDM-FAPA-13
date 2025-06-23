from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'blocos'

router = routers.DefaultRouter()
router.register('', views.BlocoViewSet, basename='blocos')

urlpatterns = [
    path('', include(router.urls))
]
