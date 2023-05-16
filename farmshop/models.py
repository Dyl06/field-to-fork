from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Product(models.Model):
    product = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    product_featured_image = CloudinaryField('image', default='placeholder')
    product_description = models.TextField()
    items = models.CharField(max_length=100, unique=True)
    items_featured_image = CloudinaryField('image', default='placeholder')
    items_description = models.TextField()
    weight = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    likes = models.ManyToManyField(User, related_name='item_likes', blank=True)

    def __str__(self):
        return self.items

    def accumulated_likes(self):
        return self.likes.count()
