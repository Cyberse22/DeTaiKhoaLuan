from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


class ChucVu(models.TextChoices):
    SINHVIEN = 'sinhvien', 'Sinh Viên'
    GIANGVIEN = 'giangvien', 'Giảng Viên'
    GIAOVU = 'giaovu', 'Giáo Vụ'


class NguoiDung(AbstractUser):
    UID = models.CharField(null=False, primary_key=True, unique=True, max_length=10)
    avatar = CloudinaryField('avatar', null=True)
    chucvu = models.CharField(max_length=20, choices=ChucVu.choices, default=ChucVu.SINHVIEN)
