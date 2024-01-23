from rest_framework.serializers import ModelSerializer
from .models import User, KhoaLuan, HoiDongBaoVe, DiemKhoaLuan


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'chucvu']


class KhoaLuanSerializer(ModelSerializer):
    class Meta:
        model = KhoaLuan
        fields = '__all__'


class HoiDongBaoVeSerializer(ModelSerializer):
    class Meta:
        model = HoiDongBaoVe
        fields = '__all__'


class DiemKhoaLuanSerializer(ModelSerializer):
    class Meta:
        model = DiemKhoaLuan
        fields = '__all__'
