from django.db import models
from nguoidung.models import NguoiDung


class KhoaLuan(models.Model):
    idkhoaluan = models.CharField(max_length=10, unique=True, primary_key=True, null=False)
    tenkhoaluan = models.CharField(max_length=255, null=False)
    sinhvien = models.ManyToManyField(NguoiDung, related_name='sinhvienkhoaluan')
    giangvienhuongdan = models.ManyToManyField(NguoiDung, related_name='giangvienhuongdan')
    ngaybaove = models.DateField()
    dabaove = models.BooleanField(default=False)