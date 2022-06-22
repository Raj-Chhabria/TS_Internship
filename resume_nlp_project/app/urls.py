from . import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('show/',views.show),
    path('skills/',views.skill_percent)
]