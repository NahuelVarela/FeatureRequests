from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth_page/', views.auth_page, name='auth_page'),
    ]