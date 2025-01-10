import threading
from django.shortcuts import redirect, render
from django.contrib import messages
from users.forms import RegisterForm
from users.models import CustomUserModel
from users.utils import send_email_confirmation
from users.utils import default_token_generator


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
            
            email_thread = threading.Thread(target=send_email_confirmation, args=(user, request))
            email_thread.start()

            messages.success(request, 'Please, confirm your email or login')
            return redirect('users:login')
        else:
            messages.error(request, form.error_messages)        
            return render(request, 'auth/register.html')

def confirm_email(request, uid, token):
    try:
        user = CustomUserModel.objects.get(id=uid)
    except CustomUserModel.DoesNotExist:
        return redirect('users:login')
    
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your email address id verified')
        return redirect('users:login')
    else:
        messages.success(request, 'Link is not correnct')
        return redirect('users:login')