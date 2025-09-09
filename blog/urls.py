from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/new/', views.create_post, name='blog-create'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post/<int:post_id>/edit/', views.edit_post, name='post-edit'),   # changed
    path('post/<int:post_id>/delete/', views.delete_post, name='post-delete'),  # changed
]


