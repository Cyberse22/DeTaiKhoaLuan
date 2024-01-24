from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError


class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class ChucVu(models.TextChoices):
    SINHVIEN = 'sinhvien', 'Sinh Viên'
    GIANGVIEN = 'giangvien', 'Giảng Viên'
    GIAOVUKHOA = 'giaovukhoa', 'Giáo Vụ Khoa'


class User(AbstractUser):
    avatar = CloudinaryField('avatar',  null=True)
    chucvu = models.CharField(max_length=20, choices=ChucVu.choices, default=ChucVu.SINHVIEN)

    class Meta:
        ordering = ['id']


class KhoaLuan(BaseModel):
    idkhoaluan = models.CharField(null=False, primary_key=True, unique=True, max_length=10)
    tenkhoaluan = models.CharField(null=False, max_length=255)
    sinhvien = models.ManyToManyField(User, through="SinhVienThucHien", related_name="khoaluan_sv")
    giangvien = models.ManyToManyField(User, through="GiangVienHuongDan", related_name="khoaluan_gv")
    ngaybaove = models.DateField()
    dabaove = models.BooleanField(default=False)


class SinhVienThucHien(BaseModel):
    khoaluan = models.ForeignKey(KhoaLuan, on_delete=models.RESTRICT)
    sinhvien = models.ForeignKey(User, on_delete=models.RESTRICT)

    class Meta:
        unique_together = ['sinhvien', 'khoaluan']

    def clean(self): #Kiểm tra số lượng
        if SinhVienThucHien.objects.filter(khoaluan=self.khoaluan).count() >= 2:
            raise ValidationError("Tối đa chỉ được hai sinh viên cho một khóa luận.")


class GiangVienHuongDan(BaseModel):
    khoaluan = models.ForeignKey(KhoaLuan, on_delete=models.RESTRICT)
    giangvien = models.ForeignKey(User, on_delete=models.RESTRICT)

    class Meta:
        unique_together = ['giangvien', 'khoaluan']

    def clean(self): #Kiểm tra số lượng
        if GiangVienHuongDan.objects.filter(khoaluan=self.khoaluan).count() >= 2:
            raise ValidationError("Tối đa hai giảng viên hướng dẫn.")


class HoiDongBaoVe(BaseModel):
    tenhoidong = models.CharField(max_length=255, unique=True, null=True)
    chutich = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='chutich')
    thuky = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='thuky')
    phanbien = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='phanbien')
    thanhvienkhac = models.ManyToManyField(User, related_name='thanhvienkhac')
    khoaluan = models.ManyToManyField(KhoaLuan, related_name='khoaluan')


class DiemKhoaLuan(BaseModel):
    khoaluan = models.ForeignKey(KhoaLuan, on_delete=models.RESTRICT, related_name='diemkhoaluan')
    hoidongchamdiem = models.ForeignKey(HoiDongBaoVe, on_delete=models.RESTRICT, related_name='hoidongchamdiem')
    diem = models.DecimalField(max_digits=5, decimal_places=2)
    nhanxet = RichTextField()

