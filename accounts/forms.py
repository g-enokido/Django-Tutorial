from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Blog


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        profile_icon = forms.ImageField(label='アイコン')
        fields = ['username', 'email', ]


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        profile_icon = forms.ImageField(label='アイコン')
        fields = ('username', 'profile_icon', 'self_introduction')


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_name', 'blog_detail', ]


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
