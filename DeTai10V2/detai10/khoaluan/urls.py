from django.urls import path, include
from rest_framework import routers
from khoaluan import views


routers = routers.DefaultRouter()
routers.register('khoaluans', views.KhoaLuanViewSet, basename='khoaluans')

urlpatterns = [
    path('', include(routers.urls))
]