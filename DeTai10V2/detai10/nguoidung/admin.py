from django.contrib import admin
from django.template.response import TemplateResponse
from django.utils.safestring import mark_safe
from django.urls import path
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from nguoidung.models import NguoiDung
from nguoidung import dao


class NguoiDungAppAdminSite(admin.AdminSite):
    admin.site.site_header = "Profile User"

    def get_urls(self):
        return [
            path('name-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats.html',{
            "stats": dao.count_name_by_user_id()
        })


admin.site.register(NguoiDung)