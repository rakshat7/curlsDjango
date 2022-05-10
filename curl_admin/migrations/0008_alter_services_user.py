# Generated by Django 3.2.9 on 2022-02-24 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curl_admin', '0007_auto_20220224_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
