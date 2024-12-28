from django.urls import path
from recipies.views import recipies_category_list_view, recipies_list_view

app_name = 'recipies'

urlpatterns = [
    path('', recipies_list_view, name='list'),
    path('categories/', recipies_category_list_view, name='categories')
]
