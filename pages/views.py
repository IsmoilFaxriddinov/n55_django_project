from django.shortcuts import render
from pages.forms import ContactForm
from pages.models import ContactModel

def home_page_view(request):
    return render(request, 'index.html')

def about_page_view(request):
    return render(request, 'pages/about.html')

def contact_page_view(request):
    if request.method == 'GET':
        return render(request, 'pages/contact.html')
    elif request.method == "POST":
        data = dict(request.POST)
        data.pop('csrfmiddlewaretoken')
        ContactModel.objects.create(name=data['name'], email=data['email'], subject=data['subject'], text=data['text'])

        return render(request, 'pages/contact.html')

