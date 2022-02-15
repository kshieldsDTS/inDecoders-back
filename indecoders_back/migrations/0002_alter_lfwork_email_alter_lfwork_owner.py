# Generated by Django 4.0.2 on 2022-02-15 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('indecoders_back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lfwork',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='lfwork',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LFWorkowner', to=settings.AUTH_USER_MODEL),
        ),
    ]