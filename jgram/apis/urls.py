from django.urls import path

from apis.views import UserCreateView, UserLoginView


urlpatterns = [
    path('v1/users/create', UserCreateView.as_view(),name = 'api_v1_user_create'),
    path('v1/users/login', UserLoginView.as_view(),name = 'api_v1_user_login'),

]