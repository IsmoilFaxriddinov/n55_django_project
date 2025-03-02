# Generated by Django 5.1.4 on 2025-01-05 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_contactmodel_created_ad_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=13)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
    ]
