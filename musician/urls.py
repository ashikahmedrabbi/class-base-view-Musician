from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_musician.as_view(), name='add_musician')
]