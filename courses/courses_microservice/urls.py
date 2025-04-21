from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_page),
    path("create-course/", views.create_course_page),
    path("edit-course/", views.edit_course_page),
    path("<slug:slug>/", views.course_details_page),
]
