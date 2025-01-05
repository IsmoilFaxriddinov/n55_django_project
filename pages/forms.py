from django import forms

from pages.models import ContactModel

class ContactForm(forms.Form):
    name = forms.CharField(max_length=125)
    email = forms.EmailField()
    subject = forms.CharField(max_length=225)
    text = forms.Textarea() 
