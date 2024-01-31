import datetime

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, parsers, status
from rest_framework.decorators import action
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from thesis.models import User, HoiDongBaoVe, DiemKhoaLuan, KhoaLuan
from thesis.serializers import UserSerializer, UserChangePasswordSerializer, HoiDongBaoVeSerializer, \
    SinhVienThesisSerializer, GiaoVuKhoaThesisSerializer, DiemKhoaLuanSerializer
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

    @action(methods=['get'], url_path='user/(?P<role>\w+)', url_name='user', detail=False)
    def current_user(self, request, role):
        if role == 'sinhvien':
            response_data = {'role': 'sinhvien'}

        elif role == 'giangvien':
            response_data = {'role': 'giangvien'}

        elif role == 'giaovukhoa':
            response_data = {'role': 'giaovukhoa'}

        elif role == 'admin':
            response_data = {'role': 'admin'}

        else:
            response_data = {'error': 'Vai trò không hợp lệ'}

        return JsonResponse(response_data)

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


class SinhVienThesisViewSet(viewsets.ModelViewSet):
    serializer_class = SinhVienThesisSerializer
    queryset = KhoaLuan.objects.all()

    def perform_create(self, serializer):
        serializer.save(sinhvien=self.request.user)


class GiaoVuKhoaThesisViewSet(viewsets.ModelViewSet):
    serializer_class = GiaoVuKhoaThesisSerializer
    queryset = KhoaLuan.objects.all()

    def perform_update(self, serializer):
        serializer.save(daxacnhan=True, ngaybaove=datetime.datetime.date())


class HoiDongBaoVeViewSet(viewsets.ModelViewSet):
    queryset = HoiDongBaoVe.objects.filter()
    serializer_class = HoiDongBaoVeSerializer
    pagination_class = paginators.GuardPaginator

    def get_permissions(self):
        if self.action == 'giaovukhoa_action':
            return [permissions.IsAuthenticated(), perms.IsGiaoVuKhoa()]
        elif self.action == 'admin_action':
            return [perms.IsAdmin()]
        return [permissions.AllowAny()]

    @action(methods=['post'], detail=True)
    def them_giangvien(self, request, pk=None):
        hoidongbaove = self.get_object()

        if not perms.IsGiaoVuKhoa().has_permission(request, self):
            return Response({"message": "Bạn không có quyền thêm giảng viên vào hội đồng"},
                            status=status.HTTP_403_FORBIDDEN)

        user_data = request.data.get('user', {})
        chucvu = user_data.get('chucvu')

        if chucvu != 'giangvien':
            return Response({"error": "Người dùng không phải là giảng viên"}, status=status.HTTP_400_BAD_REQUEST)

        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()

            hoidongbaove.giangvien_set.add(user)

            return Response({"message": "Thêm giảng viên vào hội đồng thành công"},status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Dữ liệu không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)


class DiemKhoaLuanViewSet(viewsets.ModelViewSet):
    queryset = DiemKhoaLuan.objects.filter()
    serializer_class = DiemKhoaLuanSerializer
    pagination_class = paginators.GradePaginator

    @action(detail=True, methods=['post'])
    def grade_update(self, request, pk=None):
        diemkhoaluan = self.get_object()

        if not perms.IsGiaoVuKhoa or not perms.IsAdmin:
            return Response({"message": "Bạn không có quyền cập nhật điểm"}, status=status.HTTP_403_FORBIDDEN)

        diem_data = request.data.get('diem', None)

        if diem_data is None:
            return Response({"error": "Dữ liệu không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)

        diemkhoaluan.diem = diem_data
        diemkhoaluan.save()

        return Response({"message": "Cập nhật điểm khóa luận thành công"}, status=status.HTTP_200_OK)