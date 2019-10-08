from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='top_page'),
    path('signup/', include('signup.urls')),
    path('userpage/', include('user.urls')),
    path('drafts/<int:pk>', views.post_draft_list, name='post_draft_list'),
    path('create/<int:pk>/', views.post_new, name='post_new'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('<int:pk>/', views.post_list, name='post_list'),
    path('article/<int:pk>/', views.post_detail, name='post_detail'),
    path('article/<int:pk>/comment/', include('comment.urls')),
]
