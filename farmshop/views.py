from django.shortcuts import render, get_list_or_404, redirect
from .models import Product, Order
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import generic, View
from datetime import datetime


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html',
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

    def get_orders(self, request):
        current_user_id = request.user.id
        queryset = Order.objects.filter(user_id=current_user_id)
        user_orders = get_list_or_404(queryset)

        for order in user_orders:
            order.products_list = order.products.all().values()

        return user_orders

    def get(self, request, *args, **kwargs):

        user_orders = self.get_orders(request)

        return render(
            request,
            'my_orders.html',
            {
                "order_list": user_orders,
            },
        )

    def post(self, request, *args, **kwargs):

        # Check the action
        action = request.POST['action']

        if action == "delete":

            # Get order ID from POST from form
            order_id = request.POST['order_id']

            # Load the Order
            order_obj = Order.objects.get(id=order_id)

            # Delete the Order
            order_obj.delete()

            user_orders = self.get_orders(request)

        return render(
            request,
            'my_orders.html',
            {
                "order_list": user_orders,
                "message": f"Order Number {order_id}: Deleted Successfully"
            },
        )


# class RegisterRequest(View):
#     def register_request(request):

#         if request.method == "POST":
#             form = NewUserForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 login(request, user)
#                 messages.success(request, "Registration succesful.")
#                 return redirect(HomePage(View))
#             messages.error(request,
#                            "Unsuccessful registration. Invalid information.")
#         form = NewUserForm()

#         return render(
#             request,
#             'register.html',
#             {
#                 "register_form": form
#             },
#         )


class RegisterRequest(View):

    def get(self, request, *args, **kwargs):
        return render(
           request,
           'register.html',
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration succesful.")
                return redirect('/product/beef/')
            messages.error(request,
                           "Unsuccesful registration. Invalid information.")
        form = NewUserForm()

        return render(
            request,
            'register.html',
            {
                "register_form": form
            },
        )
