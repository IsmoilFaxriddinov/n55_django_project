from django.shortcuts import render
from shop.models import ProductModel

product = ProductModel.objects.all()
context = {
    'product': product
}

def product_list_view(request):
    return render(request, 'shop/product-list.html', context)
