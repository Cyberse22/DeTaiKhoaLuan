# Generated by Django 4.2.6 on 2024-01-24 13:40

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0003_alter_user_options_alter_diemkhoaluan_nhanxet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='avatar'),
        ),
    ]
