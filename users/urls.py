from django.urls import path

from users.views import register_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', register_view, name="login"),
    path('confirm/email/<int:uid>/<token:token>/', register_view, name="confirm_email")
]
