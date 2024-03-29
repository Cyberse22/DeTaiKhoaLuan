# Generated by Django 4.2.6 on 2024-01-25 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import thesis.models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0006_hoidongbaove_tenhoidong'),
    ]

    operations = [
        migrations.AddField(
            model_name='khoaluan',
            name='baikhoaluan',
            field=models.FileField(default=thesis.models.baikhoaluan_default, upload_to='baikhoaluan/'),
        ),
        migrations.AlterField(
            model_name='diemkhoaluan',
            name='hoidongchamdiem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hoidongchamdiem', to='thesis.hoidongbaove'),
        ),
        migrations.AlterField(
            model_name='diemkhoaluan',
            name='khoaluan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diemkhoaluan', to='thesis.khoaluan'),
        ),
        migrations.AlterField(
            model_name='giangvienhuongdan',
            name='giangvien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='giangvienhuongdan',
            name='khoaluan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thesis.khoaluan'),
        ),
        migrations.AlterField(
            model_name='hoidongbaove',
            name='chutich',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chutich', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hoidongbaove',
            name='phanbien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phanbien', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hoidongbaove',
            name='thuky',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thuky', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sinhvienthuchien',
            name='khoaluan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thesis.khoaluan'),
        ),
        migrations.AlterField(
            model_name='sinhvienthuchien',
            name='sinhvien',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
