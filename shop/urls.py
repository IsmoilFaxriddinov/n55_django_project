from django.urls import path

from shop.views import shop_page_view

app_name = 'shop'

urlpatterns = [
    path('', shop_page_view)
]
