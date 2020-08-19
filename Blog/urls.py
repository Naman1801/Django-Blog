from django.contrib import admin
from django.urls import path
from Blog import views
from .views import (
    PostUpdateView,
    PostDeleteView
    # PostListView,
    # PostDetailView,
    # PostCreateView,
)

urlpatterns = [
    # path('', PostListView.as_view(), name='blog-home'),
    path('create', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
    path('<str:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<str:slug>/delete', PostDeleteView.as_view(), name='post-delete')
]