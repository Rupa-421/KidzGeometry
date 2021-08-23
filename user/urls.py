from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login/',views.signin,name="signin"),
    path('register/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
]