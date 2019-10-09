from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username', ]


admin.site.register(User, CustomUserAdmin)
