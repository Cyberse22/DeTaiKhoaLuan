from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, parsers, status
from rest_framework.decorators import action

from thesis.models import User, KhoaLuan, HoiDongBaoVe, DiemKhoaLuan
from thesis.serializers import UserSerializer, UserChangePasswordSerializer, KhoaLuanSerializer, HoiDongBaoVeSerializer, \
    DiemKhoaLuanSerializer
from thesis import perms, serializers, paginators


class UserViewSet(viewsets.ModelViewSet, generics.CreateAPIView, generics.UpdateAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer
    pagination_class = paginators.UserPaginator
    parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action.__eq__('current_user'):
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_path='current_user', url_name='current-user', detail=False)
    def current_user(self, request):
        return Response(serializers.UserSerialzier(request.user).data)

    @action(methods=['put'], detail=True)
    def chang_password(self, request, pk=None):
        user = self.get_object()
        serializers = UserChangePasswordSerializer(data=request.data)

        if serializers.is_valid():  # Kiểm tra mật khẩu cũ
            if not user.check_password(serializers.validated_data['old_password']):
                return Response({'old_password': 'Mật khẩu không đúng.'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializers.validated_data['new_password'])
            user.save()

            return Response({'message': 'Mật khẩu đã được thay đổi.'}, status=status.HTTP_200_OK)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class KhoaLuanViewSet(viewsets.ModelViewSet):
    queryset = KhoaLuan.objects.filter()
    serializer_class = KhoaLuanSerializer


class HoiDongBaoVeViewSet(viewsets.ModelViewSet):
    queryset = HoiDongBaoVe.objects.filter()
    serializer_class = HoiDongBaoVeSerializer


class DiemKhoaLuanViewSet(viewsets.ModelViewSet):
    queryset = DiemKhoaLuan.objects.filter()
    serializer_class = DiemKhoaLuanSerializer
