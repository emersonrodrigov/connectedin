# Generated by Django 2.0.7 on 2018-07-25 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_auto_20180725_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(default=uuid.uuid1, on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL),
        ),
    ]