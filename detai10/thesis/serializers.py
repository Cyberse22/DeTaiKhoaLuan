from rest_framework.serializers import ModelSerializer
from .models import User, KhoaLuan, HoiDongBaoVe, DiemKhoaLuan
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar', 'first_name', 'last_name', 'password', 'email', 'chucvu']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        data = validated_data.copy()

        user = User(**data)
        user.set_password(data['password'])
        user.save()

        return user


class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)

    def validate(self, data):
        new_password = data.get('new_password')
        confirm_new_password = data.get('confirm_new_password')

        if new_password != confirm_new_password:
            raise serializers.ValidationError("Mật khẩu mới và xác nhận mật khẩu không khớp")

        return data


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
        fields = ['khoaluan', 'hoidongchamdiem', 'diem', 'nhanxet']
