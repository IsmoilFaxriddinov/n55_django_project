from django.urls import path

from blogs.views import blog_page_view

urlpatterns = [
    path('', blog_page_view, name='list')
]
