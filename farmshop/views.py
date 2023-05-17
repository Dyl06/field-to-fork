from django.shortcuts import render
from .models import Product
from django.views import generic, View


class PostList(View):

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(category=Product.BEEF)
        #  post = get_object_or_404(queryset, slug=slug)
    
        return render(
            request,
            'product.html',
            {
                "products": products,
            },
        )