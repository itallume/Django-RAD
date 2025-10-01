from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('home/', views.blog.get, name='home'),
    path('home/<str:nome>/<int:numero>', views.blog.home, name='home_param'),
    path('info/<str:numerotel>', views.blog.contato, name='contato'),
    path('info/', views.blog.info),
    path("homeTop/", views.blog.homeTop , name=""),
    path("about/", views.blog.about)
]