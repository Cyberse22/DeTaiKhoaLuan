from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from khoaluan.models import KhoaLuan


class KhoaLuanAppAdminSite(admin.AdminSite):
    admin.AdminSite.site_header = "KhoaLuan"


admin.site.register(KhoaLuan)
