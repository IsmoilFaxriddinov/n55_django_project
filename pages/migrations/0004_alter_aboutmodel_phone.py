# Generated by Django 5.1.4 on 2025-01-05 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_aboutmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
