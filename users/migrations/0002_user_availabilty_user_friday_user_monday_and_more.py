# Generated by Django 4.0.2 on 2022-02-13 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='availabilty',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='friday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='monday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='payrate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='portfolio',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='saturday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='sunday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='thursday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='tuesday',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='wednesday',
            field=models.BooleanField(default=False),
        ),
    ]
