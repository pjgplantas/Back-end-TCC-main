# Generated by Django 4.0.6 on 2022-08-08 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pjgplantas', '0002_midia_delete_curtida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midia',
            name='local',
        ),
    ]
