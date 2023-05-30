from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('products/<str:category>',
         views.CategoryList.as_view(), name='product_list'),
    path('order/<str:category>',
         login_required(views.PlaceOrder.as_view()), name='place_order'),
    path('basket/', login_required(views.Basket.as_view()),
         name='basket'),
    path('my_orders/', login_required(views.OrderList.as_view()),
         name='orders'),
    path('register/', views.RegisterRequest.as_view(), name='register'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
 ]
