from nguoidung.models import NguoiDung
from rest_framework import serializers


class NguoiDungSerializer(serializers.ModelSerializer):
    class Meta:
        model = NguoiDung
        fields = ['UID', 'first_name', 'last_name', 'username', 'email', 'password', 'avatar', 'chucvu']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        data = validated_data.copy()
        u = NguoiDung(**data)
        u.set_password(u.password)
        u.save()

        return u
