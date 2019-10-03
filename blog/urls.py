from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='top_page'),
    path('<int:pk>/', views.post_list, name='post_list'),
    path('article/<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('login/', include('django.contrib.auth.urls')),
    path('signup/', include('signup.urls')),
    path('/<int:pk>/comment/', include('comment.urls')),
]
