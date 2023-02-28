from django.contrib import admin
from django.urls import path
from . import views

app_name="Auth_App"

urlpatterns = [
    path('',views.home,name="home"),
    path('user_registration',views.user_registration,name="register"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout")

]

