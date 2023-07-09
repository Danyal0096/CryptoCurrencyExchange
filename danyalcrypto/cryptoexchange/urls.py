from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.register, name="register"),
    path("", views.home, name="home"),
    path("profile/", views.profileSettings, name="profile"),
    path("coins/", views.cryptos, name="coins"),
    path("purchase/<str:pk>", views.purchase, name="purchase"),
]
