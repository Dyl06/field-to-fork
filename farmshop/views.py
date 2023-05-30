from django.shortcuts import render, get_list_or_404, redirect
from .models import Product, Order, UserItem
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
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


class PlaceOrder(View):

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

    # def post(self, request, *args, **kwargs):
    #     if not request.user.is_authenticated:
    #         login_required("/login")
    #     else:
    #         new_order = self.new_order(request, User)


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
                messages.info(request, "Successfully Registered")
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                else:
                    return redirect('/')
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


class Login(View):

    def get(self, request, *args, **kwargs):
        return render(
           request,
           'login.html',
        )

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if 'next' in request.GET:
                        return redirect(request.GET['next'])
                    else:
                        return redirect('/')
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()

        return render(
            request,
            'login.html',
            {
                "login_form": form
            },
        )


class Logout(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect('/')


class Basket(View):

    def get(self, request, *args, **kwargs):

        basket_items = UserItem.objects.filter(user=request.user)

        return render(
            request,
            'cart.html',
            {
                "basket_items": basket_items,
            },
        )

    def post(self, request, *args, **kwargs):

        # Check the action
        action = request.POST['action']

        if action == "add_to_basket":

            # Get order ID from POST from form
            product_id = request.POST['product_id']

            # Load the Product
            product_obj = Product.objects.get(id=product_id)

            user = request.user

            new_basket_item = UserItem(products=product_obj,
                                       user=user,
                                       quantity=1)
            new_basket_item.save()

            messages.info(request, "Added to basket")

            return redirect("/basket/")


    # def add_to_cart(request, product_id, quantity):
    #     product = Product.objects.get(id=product_id)
    #     cart = Basket(request)
    #     cart.add(product, product.unit_price, quantity)

    # def remove_from_cart(request, product_id):
    #     product = Product.objects.get(id=product_id)
    #     cart = Basket(request)
    #     cart.remove(product)

    # def get_cart(request):
    #     return render(
    #         request,
    #         'cart.html',
    #         {
    #             'cart': Basket(request)
    #         },
    #     )
