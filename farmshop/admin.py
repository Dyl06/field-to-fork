from django.contrib import admin
from .models import Product, Order

# Register Product and Order models to allow access and editing
# in admin panel.
admin.site.register(Product)
admin.site.register(Order)
