from khoaluan.models import KhoaLuan
from rest_framework import serializers


class KhoaLuanSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhoaLuan
        field = '__all__'
