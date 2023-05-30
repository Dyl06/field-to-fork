from django.contrib import admin
from .models import Product, Order, UserItem, OrderItem

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UserItem)
admin.site.register(OrderItem)


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('created_on', 'user_id', 'products')