# Generated by Django 3.2.19 on 2023-05-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmshop', '0005_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('beef', 'beef'), ('lamb', 'lamb'), ('chicken', 'chicken')], default='beef', max_length=100),
        ),
    ]
