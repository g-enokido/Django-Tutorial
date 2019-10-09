from django.urls import path
from . import views

urlpatterns = [path('<int:pk>/', views.ShowsUserPage, name="user_page"),
               path('show/<int:pk>/', views.ShowsUserPage, name='show_user'), ]
