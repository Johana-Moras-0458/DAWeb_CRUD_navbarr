from django.urls import path
from app_base import views

urlpatterns = [
    #inicio tienda de peluches
    path('',views.inicio),
]