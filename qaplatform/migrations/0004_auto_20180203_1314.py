# Generated by Django 2.0 on 2018-02-03 07:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qaplatform', '0003_auto_20180203_1312'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sess',
            new_name='Session',
        ),
    ]
