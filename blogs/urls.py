from django.urls import path
from blogs.views import blog_page_view

app_name = 'blogs'

urlpatterns = [
    path('', blog_page_view, name='list')
]
