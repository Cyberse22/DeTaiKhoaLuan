from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('thesis', views.KhoaLuanViewSet)
router.register('guard', views.HoiDongBaoVeViewSet)
router.register('grade', views.DiemKhoaLuanViewSet)

urlpatterns = [
    path('', include(router.urls))
]
