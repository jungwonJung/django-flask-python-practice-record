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
from django.contrib import admin  # django 에서 제공해주는 admin 기능을 가져다가 사용하겠습니다
from django.urls import path, include # django.urlsURLconf 에서 path 와 include 함수를 가져와서 사용하겠다 
from rest_framework import permissions  #  rest_framework 에서 제공하는 permissions (승인) 37번코드에서 설명예정
from drf_yasg.views import get_schema_view # drf_yasg의 views 에서 get_schema_view type 을 가져오겠다
from drf_yasg import openapi # api 문서화를위해 swagger를 사용하는데 swagger 메인페이지 아무값도없는 swagger 화면에서 내가지금 만드는 api 의 정보를 설명하기위해 가져온다

""" path  ( 경로 , 보기 , kwargs = None , 이름 = None ) 에 포함 할 요소를 반환합니다
 include : config.url 에 포함되어야하는 다른 URLconf 모듈에 대한 코드를 PYthon 다른 파일에서 가져오기 경로를 설정하는 함수
 """



schema_view = get_schema_view(
   openapi.Info(
      title="sDesign API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",  # 회사 주소
      contact=openapi.Contact(email="wjdwjd1501@gmail.local"),  # 회사 메일 추가
      license=openapi.License(name="JUNGganzi License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


"""  openapi 의 정보 입력
        title 은 swagger 내에서의 이름을 표시해줍니다 화면에서 볼경우 가장 크게보일것이고
        그 이름옆에 쪼꼬맣게 버젼을 표시할수도있다 v1 이라고 쪼꼬맣게 표시되는걸 확인가능해요
        내용도 적을수있는데 여기서는 test 라고 적었습니다
        서비스를 제공하는회사의 주소도 추가할수가있습니다 나중에 정말 회사가 생기면 그회사주소를 넣고싶어요
        만약 누군가 우리회사에 접촉을하고싶다면 회사이메일을추가하거나 프로젝트를만든사람의 이메일을 넣어도되겟죠
        라이센스권은 프로젝트를 만든 저에게 있습니다 
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('register.urls')),
    path('expenses/', include('expenses.urls')),
    path('income/', include('income.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # 메인페이지를 스웨거 기본홈으로 보여주겠다
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

"""
URL 형식을 로컬주소나 기본URL 뒤에 /admin이 추가로 붙는경우 admin 사이트를보여줄겁니다.이 경로는 admin을 보여주는 urls 입니다
django 에서 migrate 를 하게되면 auth_login 등등 기본적으로 제공하는 schema,table 생성됩니다
/auth 로 접속을하게되는경우 register 라는 프로젝트 app 내부에있는 urls.py 파일을 포함할겁니다
/'' 가장기본적으로 로컬로 예를들면 127.0.0.1:8000 포트로 접속시 schema_view를 swagger 를 연동한 화면으로 보여줄겁니다
추후에 나오지만 제가 만든 serializers 에서나 views에서 설정한 api 형식을 json 형태로 문서화하여 보여줄겁니다
관련된정보에대한 문서는 /redoc 이라는 주소로 접속하게되는경우 좀더 상세하게 확인가능합니다
   
"""