from django.contrib import admin
from django.contrib.auth.models import Permission, Group, User
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from django import forms
from django.urls import path

from .models import User, HoiDongBaoVe, KhoaLuan, DiemKhoaLuan, SinhVienThucHien, GiangVienHuongDan


class ThesisAdminSite(admin.AdminSite):
    site_header = 'Quản Lý Khóa Luận'

    # def get_urls(self):
    #     return [
    #         path('thesis-stats/', self.thesis_stats)
    #     ] + super().get_urls()

    # def thesis_stats(self, request): diemkhoaluan_count = DiemKhoaLuan.objects.count() stats =
    # DiemKhoaLuan.objects.annotate(khoaluan_count=Count('diemkhoaluan')).value("idkhoaluan", "tenkhoaluan",
    # "diemkhoaluan_count")
    #
    #     return TemplateResponse(request, 'admin/thesis-stats.html', {
    #         'thesis-count': diemkhoaluan_count
    #     })


admin_site = ThesisAdminSite(name='myadmin')


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'date_joined']
    list_filter = ['id', 'date_joined']
    search_fields = ['id', 'first_name', 'last_name']
    readonly_fields = ['avatar']

    def avatar_image(self, obj):
        return mark_safe(
            '<img src="static/{url}" width="120" />'.format(url=obj.image.name)
        )

    class Media:
        css = {
            'all': ('/static/css/style.css',)
        }
        js = ('/static/js/script.js',)



class SinhVienThucHienInline(admin.TabularInline):
    model = SinhVienThucHien
    extra = 2


class GiangVienHuongDanInline(admin.TabularInline):
    model = GiangVienHuongDan
    extra = 2


class KhoaLuanAdmin(admin.ModelAdmin):
    inlines = [SinhVienThucHienInline, GiangVienHuongDanInline]


admin_site.register(User, UserAdmin)
admin_site.register(HoiDongBaoVe)
admin_site.register(KhoaLuan, KhoaLuanAdmin)
admin_site.register(DiemKhoaLuan)
admin_site.register(Permission)
admin_site.register(Group)
