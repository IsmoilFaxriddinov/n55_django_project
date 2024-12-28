from django.urls import path
from recipies.views import recipies_list_view

app_name = 'recipies'

urlpatterns = [
    path('', recipies_list_view, name='list')
]
