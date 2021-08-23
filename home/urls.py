from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('listen/',views.listen,name='listen'),
    path('explore/',views.explore,name='explore'),
    path('add/',views.add,name='add'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('edit/<str:pk>/',views.edit,name="edit"),
    path('project/',views.project,name="project"),
]