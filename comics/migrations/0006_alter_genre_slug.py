# Generated by Django 4.1 on 2022-08-25 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0005_genre_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
