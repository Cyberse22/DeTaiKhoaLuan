# Generated by Django 4.2.6 on 2024-01-28 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0009_rename_baove_tieuchichamdiem_tieuchi1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tieuchichamdiem',
            name='active',
        ),
        migrations.RemoveField(
            model_name='tieuchichamdiem',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='tieuchichamdiem',
            name='updated_date',
        ),
    ]
