from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('my_orders/', views.OrderList.as_view(), name='orders')
    # path('', views.BeefItems.as_view(), name='beef')
    # path('', views.LambItems.as_view(), name='lamb')
    # path('', views.ChickenItems.as_view(), name='chicken')
 ]
