from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
import forms


class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = forms.UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleand_data.get('username')
            password = form.cleand_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog/post_list.html')
        return render(request, 'create.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = forms.UserCreateForm(request.POST)
        return render(request, 'create.html', {'form': form, })


class Account_login(CreateView):
    def post(self, request, *arg, **kwargs):
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'form': form, })

    def get(self, request, *args, **kwargs):
        form = forms.LoginForm(request.POST)
        return render(request, 'login.html', {'form': form, })
