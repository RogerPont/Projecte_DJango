"""
Defineix les rutes d'URL per a l'aplicació Blog.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts_list, name='posts-list'),
    path('posts/<slug:slug>/', views.post_detail, name='posts-detail'),
    path('authors/', views.authors_list, name='authors-list'),
    path('authors/<int:author_id>/', views.author_detail, name='author-detail'),
    path('tags/', views.tags_list, name='tags-list'),
    path('tags/<str:tag>/', views.tag_posts, name='tag-posts'),
]
