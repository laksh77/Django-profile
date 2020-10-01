from django.urls import path
from . import views  # imports all the functions from views.py

urlpatterns = [
    path('', views.home),   # calls the home func from views.py
]
