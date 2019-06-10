from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth_page/', views.auth_page, name='auth_page'),
    path('', include('social_django.urls', namespace='social')),
    ]