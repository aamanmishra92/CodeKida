from django.contrib import admin
from django.urls import path
from gun2 import views

urlpatterns = [
    path('', views.index, name="home"),
    path('services', views.services, name="services"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('c', views.c, name="c"),
    path('c1', views.c1, name="c1"),
    path('c2', views.c2, name="c2"),
    path('c3', views.c3, name="c3"),
]