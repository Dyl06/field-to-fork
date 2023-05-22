from django.shortcuts import render, get_list_or_404
from .models import Product, Order
from django.contrib.auth.models import User
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
        current_user_id = request.user.id
        queryset = Order.objects.filter(user_id=current_user_id)
        user_orders = get_list_or_404(queryset)

        for order in user_orders:
            order.products = order.product_id.all().values()

        return render(
            request,
            'my_orders.html',
            {
                "order_list": user_orders,
            },
        )


# class OrderList(generic.ListView):
#    model = Order
#    template_name = "my_orders.html"
