
from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyTokenView

urlpatterns = [
    path("login/", views.login_page),
    path("register/", views.register_page),
    path("register-student/", views.register_student_page),
    path("register-teacher/", views.register_teacher_page),
    path("edit-profile/", views.edit_profile_page),
    path("control-panel/", views.control_panel_page),
    path("token/", MyTokenView.as_view(), name='token_obtain_pair'),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
