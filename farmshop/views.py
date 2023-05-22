from django.shortcuts import render
from .models import Product, Order
from django.views import generic, View



class CategoryList(View):

    def get(self, request, *args, **kwargs):
        beef_products = Product.objects.filter(category=Product.BEEF)
        lamb_products = Product.objects.filter(category=Product.LAMB)
        # chicken_products = Product.objects.filter(categories=Product.CHICKEN)
    
        return render(
            request,
            'product.html',
            {
                "beef_products": beef_products,
                "lamb_products": lamb_products,
                # "chicken_products": chicken_products,
            },
        )


class OrderList(View):
    
    def get(self, request, *args, **kwargs):
        # TODO: Find out current logged in User ID
        logged_in_user_id = 1
        user_orders = Order.objects.filter(user_id=logged_in_user_id)
    
        return render(
            request,
            'my_orders.html',
            {
                "order_list": user_orders,
            },
        )

# class BeefItems(View):
#     def get(self, request, *args, **kwargs):


# class LambItems(View):
#     def get(self, request, *args, **kwargs):


# class ChickenItems(View):
#     def get(self, request, *args, **kwargs):
