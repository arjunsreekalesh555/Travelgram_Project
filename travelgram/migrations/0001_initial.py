# Generated by Django 4.2.11 on 2024-06-12 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travelgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Place_name', models.CharField(max_length=250)),
                ('Weather', models.CharField(max_length=250)),
                ('Location', models.CharField(max_length=250)),
                ('Map', models.URLField(max_length=500)),
                ('Place_img', models.ImageField(upload_to='places/')),
                ('Description', models.TextField(max_length=5000)),
            ],
        ),
    ]
