from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("trains/", views.trains, name="trains"),
    path("passenger/", views.passenger, name="passenger"),
    path("confirmation/", views.confirmation, name="confirmation"),
]