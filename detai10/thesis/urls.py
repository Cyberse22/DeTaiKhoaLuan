from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('sinhvien', views.SinhVienThesisViewSet, basename='sinhvien')
router.register('giaovukhoa', views.GiaoVuKhoaThesisViewSet, basename='giaovukhoa')
router.register('council', views.HoiDongBaoVeViewSet, basename='council')
router.register('grade', views.DiemKhoaLuanViewSet, basename='grade')

urlpatterns = [
    path('', include(router.urls)),
]
