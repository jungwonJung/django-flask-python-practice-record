from django.urls import path
from .views import RegisterView, VerifyEmail, LoginAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('email-verify', VerifyEmail.as_view(), name="email-verify"),
]