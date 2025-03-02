# Generated by Django 5.1.4 on 2025-01-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_alter_bloglikesmodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('comment', models.TextField()),
                ('name', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Blog detail',
                'verbose_name_plural': 'Blog details',
            },
        ),
    ]
