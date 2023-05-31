import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator


# Model for all the products for sale.
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
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        validators=[MinValueValidator(0)]
    )
    likes = models.ManyToManyField(User, related_name='item_likes', blank=True)

    def __str__(self):
        return self.items

    def accumulated_likes(self):
        return self.likes.count()


# Model for product items the user has added to their basket ready for purchase
class UserItem(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)

    def line_total(self):
        return self.products.price * self.quantity

    def __str__(self):
        return self.products.items


# Model for products the user has bought in current session or previously.
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def line_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.items


# Model for creating an order
class Order(models.Model):
    created_on = models.DateTimeField()
    user_id = models.ForeignKey(User, related_name='user_id', blank=False,
                                on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem,
                                      blank=True)

    def total_price(self):
        total_price = 0
        for ordered_item in self.products.all():
            total_price += ordered_item.product.price * ordered_item.quantity

        return total_price

    def __str__(self):
        return f"{self.user_id}"

    def __str__(self):
        return self.products
