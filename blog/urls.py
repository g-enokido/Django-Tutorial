from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='top_page'),
    path('drafts/<int:pk>', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('<int:pk>/', views.post_list, name='post_list'),
    path('article/<int:pk>/', views.post_detail, name='post_detail'),
    path('article/<int:pk>/comment/', include('comment.urls')),
    path('create/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('signup/', include('signup.urls')),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove')
]
