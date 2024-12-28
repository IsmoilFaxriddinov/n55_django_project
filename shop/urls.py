from django.urls import path
from shop.views import product_list_view

app_name = 'shop'

urlpatterns = [
    path('', product_list_view, name='product-list')
]
