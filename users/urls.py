from django.urls import path

from users.views import confirm_email, register_view

app_name = 'users'

urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', register_view, name="login"),
    path('confirm/email/<int:uid>/<str:token>/', confirm_email, name="confirm_email")
]
