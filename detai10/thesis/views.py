import requests.utils
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
    def chang_password(self, request):
        user = self.get_object()
        serializer = UserChangePasswordSerializer(data=request.data)

        if serializer.is_valid():  # Kiểm tra mật khẩu cũ
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({'old_password': 'Mật khẩu không đúng.'}, status=status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.validated_data['new_password'])
            user.save()

            return Response({'message': 'Mật khẩu đã được thay đổi.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KhoaLuanViewSet(viewsets.ModelViewSet):
    queryset = KhoaLuan.objects.filter()
    serializer_class = KhoaLuanSerializer
    pagination_class = paginators.ThesisPaginator
    parser_classes = [parsers.FileUploadParser]

    def get_permissions(self):
        if self.action == 'giaovukhoa_action':
            return [permissions.IsAuthenticated(), perms.IsGiaoVuKhoa()]
        elif self.action == 'admin_action':
            return [perms.IsAdminOrReadOnly()]

        return [permissions.AllowAny()]

    @action(methods=['get'], detail=False)
    def giaovukhoa_action(self, request):
        if not perms.IsGiaoVuKhoa().has_permission(request, self):
            return Response({"message": "Bạn không có quyền truy cập"}, status=status.HTTP_403_FORBIDDEN)

        return Response(serializers.UserSerialzier(request.user).data)

    @action(methods=['get'], detail=False)
    def admin_action(self, request):
        # Kiểm tra quyền ở đây
        if not perms.IsAdminOrReadOnly().has_permission(request, self):
            return Response({"message": "Bạn không có quyền truy cập"}, status=status.HTTP_403_FORBIDDEN)

        return Response({"message": "Chỉ admin mới có thể truy cập"})

    @action(methods=['post'], detail=False)
    def giaovukhoa_action(self, request):
        khoaluan_data = request.data.get('khoaluan', {})
        sinhvien_data = request_data.get('sinhvien', [])
        giangvien_data = request_data.get('giangvien', [])

        khoaluan_serializer = KhoaLuanSerializer(data=khoaluan_data)
        if khoaluan_serializer.is_valid():
            khoaluan_instance = khoaluan_serializer.save()

            khoaluan_instance.sinhvien.set(sinhvien_data)
            khoaluan_instance.giangvien.set(giangvien_data)

            return Response({"message": "Ghi nhận khóa luận thành công"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Dữ liệu không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)

class HoiDongBaoVeViewSet(viewsets.ModelViewSet):
    queryset = HoiDongBaoVe.objects.filter()
    serializer_class = HoiDongBaoVeSerializer
    pagination_class = paginators.GuardPaginator


class DiemKhoaLuanViewSet(viewsets.ModelViewSet):
    queryset = DiemKhoaLuan.objects.filter()
    serializer_class = DiemKhoaLuanSerializer
    pagination_class = paginators.GradePaginator
