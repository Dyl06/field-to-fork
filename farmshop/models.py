import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Product(models.Model):
    BEEF = 'beef'
    LAMB = 'lamb'
    CHICKEN = 'chicken'

    CATEGORIES = (
        (BEEF, BEEF),
        (LAMB, LAMB),
        (CHICKEN, CHICKEN),
    )

    category = models.CharField(max_length=100,
                                choices=CATEGORIES,
                                default=BEEF)
    product_featured_image = CloudinaryField('image', default='placeholder')
    product_description = models.TextField()
    items = models.CharField(max_length=100, unique=True)
    items_featured_image = CloudinaryField('image', default='placeholder')
    items_description = models.TextField()
    weight = models.CharField(max_length=50)
    price = models.IntegerField()
    likes = models.ManyToManyField(User, related_name='item_likes', blank=True)

    def __str__(self):
        return self.items

    def accumulated_likes(self):
        return self.likes.count()


class Order(models.Model):
    created_on = models.DateTimeField()
    user_id = models.ForeignKey(User, related_name='user_id', blank=False, 
                                on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,
                                      related_name='products',
                                      blank=False)

    def total_price(self):
        total_price = 0
        for product in self.products.all():
            total_price += product.price

        return total_price

