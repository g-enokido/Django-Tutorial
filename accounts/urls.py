from django.urls import path
from . import views
from django.contrib.auth import views as authviews


urlpatterns = [path('new/', views.CreateUser.as_view(), name='signup'),
               path('settings/', views.Create_blog, name='blog_settings'),
               path('profile/', views.ShowsUserPage, name="user_page"),
               path('profile/edit/', views.ChangeUserData, name="user_cutomize"),
               path('profile/show/', views.GetUserData, name='show_user'),
               path('blog/delete/<int:pk>/',
                    views.Delete_blog, name='blog_delete'),
               path('login/', views.Account_login.as_view(), name='login'),
               path('logout/',
                    authviews.LogoutView.as_view(next_page='/'), name='logout'),
               path('reject/', views.Reject_user, name='reject'),
               ]
