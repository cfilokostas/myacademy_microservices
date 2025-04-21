from django.urls import path
from . import views

urlpatterns = [
    # to main service
    path("", views.index),
    # course microservice
    path('courses/', views.proxy_courses),
    path('courses/create-course/', views.proxy_courses),
    path('courses/edit-course/', views.proxy_courses),
    path("courses/<str:course_id>/", views.proxy_courses),
    # users microservice urls
    path("users/login/", views.proxy_users),
    path("users/register/", views.proxy_users),
    path("users/register-student/", views.proxy_users),
    path("users/register-teacher/", views.proxy_users),
    path("users/edit-profile/", views.proxy_users),
    path("users/control-panel/", views.proxy_users),
    # payment microservice urls
    path("payment/", views.proxy_payment),

]
