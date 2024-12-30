from django.urls import path
from blogs.views import blog_page_view, blog_detail_view

app_name = 'blogs'

urlpatterns = [
    path('<int:pk>/', blog_detail_view, name='detail'),
    path('', blog_page_view, name='list')
]
