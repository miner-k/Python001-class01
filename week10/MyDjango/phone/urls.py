from django.contrib import admin
from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('', views.show_today),
    re_path('^show/(?P<year>^[0-9]{8}$)', views.show_today),
    path('product/', views.show_product),
]