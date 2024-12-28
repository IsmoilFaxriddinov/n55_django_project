from django.shortcuts import render

def shop_page_view(request):
    return render(request, 'shop/shop.html')
