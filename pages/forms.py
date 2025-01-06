from django import forms

from pages.models import AboutModel, BlogDetailModel, ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

class AboutForm(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = '__all__'

class BlogDetailForm(forms.ModelForm):
    class Meta:
        model = BlogDetailModel
        fields = '__all__'