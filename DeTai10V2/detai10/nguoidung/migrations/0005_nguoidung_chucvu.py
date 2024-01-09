# Generated by Django 4.2.6 on 2024-01-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nguoidung', '0004_delete_chucvu'),
    ]

    operations = [
        migrations.AddField(
            model_name='nguoidung',
            name='chucvu',
            field=models.CharField(choices=[('sinhvien', 'Sinh Viên'), ('giangvien', 'Giảng Viên'), ('giaovu', 'Giáo Vụ')], default='sinhvien', max_length=20),
        ),
    ]
