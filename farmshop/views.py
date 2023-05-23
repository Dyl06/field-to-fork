from django.shortcuts import render, get_list_or_404
from .models import Product, Order
from django.contrib.auth.models import User
from django.views import generic, View
from datetime import datetime


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'home.html',
        )


class CategoryList(View):

    def get(self, request, category, *args, **kwargs):

        products = Product.objects.filter(category=category)
        product_list = get_list_or_404(products)

        return render(
            request,
            'product.html',
            {
                "products": product_list,
                "category": category,
            },
        )

    def post(self, request, *args, **kwargs):

        # Set to right now
        created_on = datetime.now()

        # Current user
        user_obj = request.user

        # Create the Order
        new_order = Order(created_on=created_on,
                          user_id=user_obj)
        new_order.save()

        # Get product ID from POST from form
        product_id = request.POST['product_id']

        # Ordered product
        product_obj = Product.objects.get(id=product_id)

        # Add to the Order
        new_order.products.add(product_obj)
        new_order.save()

        return render(
            request,
            'order_created.html',
            {
                "product": product_obj,
                "new_order": new_order
            },
        )


class OrderList(View):

    def get(self, request, *args, **kwargs):
        current_user_id = request.user.id
        queryset = Order.objects.filter(user_id=current_user_id)
        user_orders = get_list_or_404(queryset)

        for order in user_orders:
            order.products_list = order.products.all().values()

        return render(
            request,
            'my_orders.html',
            {
                "order_list": user_orders,
            },
        )

    # def post(self, request, *args, **kwargs):
    #     current_user_id = request.user.id
    #     queryset = Order.objects.filter(user_id=current_user_id)
    #     user_orders = get_list_or_404(queryset)

    #     ordered_items = order.products(data=request.POST)
    #     for order in user_orders:
    #         order.products = order.products.all().values()

    #     return render(
    #         request,
    #         'my_orders.html',
    #         {
    #             "order_list": user_orders,
    #         },
    #     )
