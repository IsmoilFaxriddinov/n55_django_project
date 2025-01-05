from django.urls import path

from pages.views import about_page_view, contact_page_view, home_page_view, test_view

app_name = "pages"

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about/', about_page_view, name='about'),
    path('sa/', test_view, name='test'),
    path('contact/', contact_page_view, name='contact')
]
