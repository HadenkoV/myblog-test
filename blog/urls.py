from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.posts),
    path('posts/<slug:slug>/', views.SinglePostView.as_view(), name='post-detail'),
] 

