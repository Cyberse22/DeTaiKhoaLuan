from rest_framework import viewsets, generics, status, parsers, permissions
from rest_framework.decorators import action
from rest_framework.views import Response
from khoaluan.models import KhoaLuan
from khoaluan import serializers, paginators


class KhoaLuanViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = KhoaLuan.objects.filter()
    serializer_class = serializers.KhoaLuanSerializer