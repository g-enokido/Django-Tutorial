from django.urls import path
from . import views
from django.contrib.auth import views as authviews


urlpatterns = [path('new/', views.CreateUser.as_view(), name='signup'),
               path('settings/', views.Create_blog, name='blog_settings'),
               path('<int:pk>/', views.ShowsUserPage, name="user_page"),
               path('show/<int:pk>/', views.GetUserData, name='show_user'),
               path('login/', views.Account_login.as_view(), name='login'),
               path('logout/',
                    authviews.LogoutView.as_view(next_page='/'), name='logout'),
               ]
