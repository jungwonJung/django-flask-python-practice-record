from django.urls import path
from .views import RegisterView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, RequestPasswordResetEmail ,SetNewPasswordAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('email-verify', VerifyEmail.as_view(), name="email-verify"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    # register app 내에있는 login view 를 사용하여 로그인할때 refresh 토큰값이 response 되는데
    # refresh 토큰값을 /auth/token/refresh/ 넣고 excute 하면 access 토큰값이 반환되게해준다
    path('request-reset-email', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(), name='password-reset-confirm' ),
    path('password-reset-complete',SetNewPasswordAPIView.as_view(), name = 'password-reset-complete')

]