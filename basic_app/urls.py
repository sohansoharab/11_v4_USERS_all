from django.urls import path, include
from basic_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.user_register, name='register'),
    # path('login', views.user_login, name='login'),

]
