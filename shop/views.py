from django.shortcuts import render
from shop.models import ProductModel

product = ProductModel.objects.all()
context = {
    'product': product
}

def product_list_view(request):
    return render(request, 'shop/product-list.html', context)

def product_detail_view(request, pk):
    product = ProductModel.objects.filter(id=pk).first()
    if product is not None:
        context = {
            'product': product
        }
        return render(request, 'shop/product_detail.html', context)
    else:
        return render(request, 'pages/404.html')

