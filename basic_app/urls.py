from django.urls import path, include
from basic_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.user_register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('new_post', views.new_post, name='new_post'),
    path('post_details/<int:pk>', views.post_details, name='post_details'),
    path('post_edit/<int:pk>', views.post_edit, name='post_edit'),
    path('post_delete/<int:pk>', views.post_delete, name='post_delete'),

]
