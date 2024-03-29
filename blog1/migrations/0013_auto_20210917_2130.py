# Generated by Django 3.0.3 on 2021-09-17 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog1', '0012_auto_20210917_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='address',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
