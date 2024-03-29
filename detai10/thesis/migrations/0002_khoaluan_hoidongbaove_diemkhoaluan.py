# Generated by Django 4.2.6 on 2024-01-23 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KhoaLuan',
            fields=[
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_date', models.DateField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('idkhoaluan', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('tenkhoaluan', models.CharField(max_length=255)),
                ('ngaybaove', models.DateField()),
                ('dabaove', models.BooleanField(default=False)),
                ('giangvienhuongdan', models.ManyToManyField(related_name='giangvienhuongdan', to=settings.AUTH_USER_MODEL)),
                ('sinhvienthuchien', models.ManyToManyField(related_name='sinhvienthuchien', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HoiDongBaoVe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_date', models.DateField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('chutich', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='chutich', to=settings.AUTH_USER_MODEL)),
                ('khoaluan', models.ManyToManyField(related_name='khoaluan', to='thesis.khoaluan')),
                ('phanbien', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='phanbien', to=settings.AUTH_USER_MODEL)),
                ('thanhvienkhac', models.ManyToManyField(related_name='thanhvienkhac', to=settings.AUTH_USER_MODEL)),
                ('thuky', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='thuky', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DiemKhoaLuan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_date', models.DateField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('diem', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nhanxet', models.TextField()),
                ('hoidongchamdiem', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='hoidongchamdiem', to='thesis.hoidongbaove')),
                ('khoaluan', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='diemkhoaluan', to='thesis.khoaluan')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
