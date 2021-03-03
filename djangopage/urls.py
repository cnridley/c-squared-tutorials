from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.djangopage, name='djangopage'),
    path('djangopage/setting_up', views.setting_up, name='setting_up'),
]