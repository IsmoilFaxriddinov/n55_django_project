from django import forms
from blogs.models import BlogCommentModel, BlogDetailModel

class BlogDetailForm(forms.ModelForm):
    class Meta:
        model = BlogDetailModel
        fields = '__all__'

class BlogCommentModelForm(forms.ModelForm):
    class Meta:
        model = BlogCommentModel
        fields = ['comment']