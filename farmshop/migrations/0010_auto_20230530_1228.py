# Generated by Django 3.2.19 on 2023-05-30 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmshop', '0009_auto_20230530_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='products',
                                         to='farmshop.Product'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
