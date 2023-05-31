# Generated by Django 3.2.19 on 2023-05-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('beef', 'beef'), ('lamb', 'lamb'),
                                            ('chicken', 'chicken')],
                                   default='beef', max_length=100),
        ),
    ]
