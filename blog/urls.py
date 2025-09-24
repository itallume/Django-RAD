from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('home/', views.blog.get),
    path('eco/<str:texto>/', views.blog.eco),
    path('info/', views.blog.info)

]