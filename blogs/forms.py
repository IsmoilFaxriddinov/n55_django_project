from django import forms
from blogs.models import BlogDetailModel

class BlogDetailForm(forms.ModelForm):
    class Meta:
        model = BlogDetailModel
        fields = '__all__'