from django.shortcuts import redirect, render
from django.contrib import messages
from users.forms import RegisterForm
from users.models import CustomUserModel

def register_view(request):
    if request.method == "GET":
        return render(request, 'auth/register.html')
    elif request.method == "POST":
        data = request.POST
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(raw_password=data['password1'])
            user.save()
            messages.success(request, 'Please, confirm your email or login')
            return redirect('users:login')
        else:
            messages.error(request, form.error_messages)
            return render(request, 'auth/register.html')