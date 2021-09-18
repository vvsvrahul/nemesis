# Generated by Django 3.0.3 on 2020-06-09 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog1', '0003_delete_blogcontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcontent1',
            name='id',
        ),
        migrations.AlterField(
            model_name='blogcontent1',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]