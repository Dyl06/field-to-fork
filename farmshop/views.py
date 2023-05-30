from django.shortcuts import render, get_list_or_404, redirect
from .models import Product, Order, UserItem, OrderItem
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


class OrderList(View):

    def get_orders(self, request):
        current_user_id = request.user.id
        queryset = Order.objects.filter(user_id=current_user_id)
        user_orders = get_list_or_404(queryset)

        for order in user_orders:
            order.products_list = order.products.all()

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

    def get_orders(self, request):
        current_user_id = request.user.id
        queryset = UserItem.objects.filter(user_id=current_user_id)
        user_orders = get_list_or_404(queryset)

        for order in user_orders:
            order.products_list = order.products.all().values()

        return user_orders

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

            user = request.user

            # Get order ID from POST from form
            product_id = request.POST['product_id']

            # Load the Product
            product_obj = Product.objects.get(id=product_id)

            # Is this product in the basket
            if UserItem.objects.filter(products=product_obj,
                                       user=user).exists():
                # Increase quantity
                order_obj = UserItem.objects.get(products=product_obj,
                                                 user=user)
                order_obj.quantity = order_obj.quantity + 1
                order_obj.save()

            else:
                # Add new order

                new_basket_item = UserItem(products=product_obj,
                                           user=user,
                                           quantity=1)
                new_basket_item.save()

            messages.info(request, "Added to basket")
        
        elif action == "update_quantity":

            user = request.user

            # Get order ID from POST from form
            product_id = request.POST['product_id']

            # Load the Product
            product_obj = Product.objects.get(id=product_id)

            order_obj = UserItem.objects.get(products=product_obj,
                                             user=user)
            order_obj.quantity = request.POST['quantity']
            order_obj.save()

            messages.info(request, "Updated quantity")

        elif action == "delete":

            # Get order ID from POST from form
            product_id = request.POST['product_id']

            product_obj = Product.objects.get(id=product_id)

            # Load the Basket Items
            order_obj = UserItem.objects.filter(products=product_obj)

            # Delete the Basket Items
            order_obj.delete()

            messages.info(request, "Deleted item from basket")

        elif action == "buy_now":

            # create new order

            # Set to right now
            created_on = datetime.now()

            # Current user
            user_obj = request.user

            # Create the Order
            new_order = Order(created_on=created_on,
                              user_id=user_obj)

            new_order.save()

            # Load the Basket Items
            item_objects = UserItem.objects.filter(user=user_obj)

            for item in item_objects:
                new_order_item = OrderItem(product=item.products,
                                           quantity=item.quantity)
                new_order_item.save()
                new_order.products.add(new_order_item)

            new_order.save()

            # Empty current basket
            item_objects.delete()


            # redirect to my orders
            return redirect("/my_orders/")

        return redirect("/basket/")

