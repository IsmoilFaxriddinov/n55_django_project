from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def send_email_confirmation(user, request):
    token = default_token_generator.make_token(user)
    uid = user.pk

    confirmation_link = request.build_absolute_uri(reverse('users:confirm_email', kwargs={'uid': uid, 'token': token}))

    subject = 'Confirm your email address'
    message = render_to_string('auth/email_confirmation.html', context={
        'user':user,
        'confirmation_link': confirmation_link,
    })
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

