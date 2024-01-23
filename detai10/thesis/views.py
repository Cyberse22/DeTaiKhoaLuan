from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from django.views import View

from .models import User, KhoaLuan, HoiDongBaoVe, DiemKhoaLuan
from .serializers import UserSerializer, KhoaLuanSerializer, HoiDongBaoVeSerializer, DiemKhoaLuanSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class KhoaLuanViewSet(viewsets.ModelViewSet):
    queryset = KhoaLuan.objects.filter()
    serializer_class = KhoaLuanSerializer


class HoiDongBaoVeViewSet(viewsets.ModelViewSet):
    queryset = HoiDongBaoVe.objects.filter()
    serializer_class = HoiDongBaoVeSerializer


class DiemKhoaLuanViewSet(viewsets.ModelViewSet):
    queryset = DiemKhoaLuan.objects.filter()
    serializer_class = DiemKhoaLuanSerializer

