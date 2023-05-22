import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Product(models.Model):
    BEEF = 'Beef'
    LAMB = 'Lamb'
    CHICKEN = 'Chicken'

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
    price = models.CharField(max_length=50)
    likes = models.ManyToManyField(User, related_name='item_likes', blank=True)
    

    def __str__(self):
        return self.items

    def accumulated_likes(self):
        return self.likes.count()


# class Order(models.Model):
#     order_number = models.UUIDField(primary_key=True, default=uuid.uuid4,
#                                     editable=False)
#     collection_date = models.DateTimeField()
#     order_items = models.Choices()
#     customer_name = models.TextField()
#     customer_email = models.EmailField()


class Order(models.Model):
    created_on = models.DateTimeField()
    user_id = models.ManyToManyField(User, related_name='user_id', blank=False)
    product_id = models.ManyToManyField(Product, related_name='product_id', 
                                        blank=False)



# class Customer(models.Model):
#     first_name =
#     last_name = 
#     email =
    
