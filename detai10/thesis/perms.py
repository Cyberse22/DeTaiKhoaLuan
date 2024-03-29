from rest_framework import permissions


class OwnerAuthenticated(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return self.has_object_permission(request, view) and request.user == obj.user


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_authenticated and request.user.is_superuser


class IsSinhVien(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.chucvu == 'sinhvien'


class IsGiangVien(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.chucvu == 'giangvien'


class IsGiaoVuKhoa(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.chucvu == 'giaovukhoa'
