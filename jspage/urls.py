from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.jspage, name='jspage'),
    path('jspage/jsbasics', views.jsbasics, name='jsbasics'),
    path('jspage/stringmethods', views.stringmethods, name='stringmethods'),
]