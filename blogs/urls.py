from django.urls import path
from blogs.views import blog_comment_view, blog_page_view, blog_detail_view

app_name = 'blogs'

urlpatterns = [
    path('<int:pk>/', blog_detail_view, name='detail'),
    path('comment/<int:blog_id>/', blog_comment_view, name="comment"),
    path('', blog_page_view, name='list')
]
