# Generated by Django 4.1 on 2022-08-19 12:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0002_alter_comic_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='chapter_count',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
