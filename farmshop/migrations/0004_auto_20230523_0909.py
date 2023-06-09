# Generated by Django 3.2.19 on 2023-05-23 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farmshop', '0003_auto_20230522_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product_id',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='products',
                                         to='farmshop.Product'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='user_id',
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(default=1,
                                    on_delete=django.db.models.deletion.CASCADE,  # noqa
                                    related_name='user_id', to='auth.user'),
            preserve_default=False,
        ),
    ]
