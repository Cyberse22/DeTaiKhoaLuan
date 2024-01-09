from django.urls import path, include
from rest_framework import routers
from nguoidung import views


routers = routers.DefaultRouter()
routers.register('nguoidungs', views.NguoiDungViewSet, basename='nguoidungs')

urlpatterns = [
    path('', include(routers.urls))
]