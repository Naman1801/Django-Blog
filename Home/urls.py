from django.contrib import admin
from django.urls import path
from django.contrib.auth.models import User
from Home import views
from .views import (
    PostListView,
    # PostUpdateView,
    # PostCreateView,
    # UserPostListView
    # PostDetailView,
    # PostDeleteView
)

urlpatterns = [
    path('',PostListView.as_view(), name='home'),
    # path('<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('contact', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    # path('logout/', views.handlelogout, name='logout'),
    # path('login/', views.handlelogin, name='login'),

]