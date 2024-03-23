from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='home'),
    path('news_detail/', views.news_detail, name='detail'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('logout/', views.logout_page, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('addpost/', views.add_post, name='addpost'),
    path('editpost/', views.edit_post, name='editpost'),

    path('about/', views.about, name='about'),
]
