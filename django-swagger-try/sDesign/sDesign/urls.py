"""sDesign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import  settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from Users import views, urls
from rest_framework.permissions import AllowAny, IsAuthenticated, BasePermission
from rest_framework_swagger.views import get_swagger_view


# schema_view = get_swagger_view(title='sDesign API')
#     openapi.Info(
#         title="sDesing User API",
#         default_version="v1",
#         description="sDesign 을 위한 API 문서 ",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="wjdwjd1501@gmail.com"),
#         license=openapi.License(name="Test License"),
#     ),
#     validators=['flex'],
#     public=True,
#     url='http://127.0.0.1:8000/', # Important bit
#     permission_classes=(AllowAny,),
#     patterns=schema_url_patterns,
# )

schema_view = get_schema_view(
   openapi.Info(
        title="sDesign User API",
        default_version="v1",
        description="sDesign 을 위한 API 문서 ",
        terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="wjdwjd1501@gmail.com"),
        license=openapi.License(name="Test License"),
   ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', schema_view, name='home'),
    # path('register',register.as_view()),
    # path('login',login.as_view()),
    path('admin/', admin.site.urls),
    path("Users/", include(("Users.urls", "Users"))),
]

# # 이건 디버그일때만 swagger 문서가 보이도록 해주는 설정이라는 듯. urlpath도 이 안에 설정 가능해서, debug일때만 작동시킬 api도 설정할 수 있음.
# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
#         re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#         re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    ]