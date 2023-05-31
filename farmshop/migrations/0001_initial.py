# Generated by Django 3.2.19 on 2023-05-16 16:01

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                 serialize=False, verbose_name='ID')),
                ('product_featured_image',
                 cloudinary.models.CloudinaryField(default='placeholder',
                                                   max_length=255,
                                                   verbose_name='image')),
                ('product_description', models.TextField()),
                ('items', models.CharField(max_length=100, unique=True)),
                ('items_featured_image',
                 cloudinary.models.CloudinaryField(default='placeholder',
                                                   max_length=255,
                                                   verbose_name='image')),
                ('items_description', models.TextField()),
                ('weight', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('likes', models.ManyToManyField(blank=True,
                                                 related_name='item_likes',
                                                 to=settings.AUTH_USER_MODEL)),
                ('product',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='products',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
