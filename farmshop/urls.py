from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.HomePage.as_view(), name='home'),
    path('products/<str:category>', views.CategoryList.as_view(),
         name='product_list'),
    path('my_orders/', views.OrderList.as_view(), name='orders')
 ]
