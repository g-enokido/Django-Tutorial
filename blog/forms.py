from django import forms
from .models import Post, Category
from django.contrib.auth.forms import AuthenticationForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        image = forms.ImageField(label='画像ファイル')
        fields = ['title', 'text', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-contorol'
        self.fields['password'].widget.attrs['class'] = 'form-contorol'
