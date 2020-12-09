from django.shortcuts import render
from rest_framework import generics, status, views
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema # swagger 내의 parameter 내용 생성코드 추가
from drf_yasg import openapi  # swagger 내의 parameter 내용 생성코드 추가
# Create your views here.
class RegisterView(generics.GenericAPIView):
   
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)  # (self = RegisterView ) ,user = request.data
        serializer.is_valid(raise_exception=True) # 보류
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])  # User 데이터베이스에서 serializer.data 중 email 이라고 user 다시 선언
 
        token = RefreshToken.for_user(user).access_token    # 여기서부터 인증이메일 보내는 코드 

        current_site = get_current_site(request).domain
        relativeLink = reverse('email-verify')

        absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
        email_body = 'hi' +user.username + '링크를 눌러 이메일을 인증해주세요 /n'+ absurl
        data = {'email_body' : email_body, 'to_email' : user.email,  'email_subject' : '이메일을 인증 해주세요!!'}
        Util.send_email(data)

        return Response(user_data,status=status.HTTP_201_CREATED)

class VerifyEmail(views.APIView):      # 이메일 인증코드관련  처음엔 generics.GenericAPIView 였지만 parameter 내용추가를 위해 변경 
    
    serializer_class = EmailVerificationSerializer 

    token_param_config = openapi.Parameter('token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING )  # 파라미터 출력내용 설정

    @swagger_auto_schema(manual_parameters=[token_param_config])        # swagger schema 설정 
    def get(self,request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email' : '이메일 인증이 완료되었습니다! '},status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error' : '이메일 인증에 실패하였습니다! '},status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error' : '토큰이 없습니다'},status=status.HTTP_400_BAD_REQUEST)

            
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        # user = request.data  처럼 나타낼수있지만 짧기때문에 바로 62번 (data=안에) 넣어준다 
        serializer = self.serializer_class(data=request.data)  
        serializer.is_valid(raise_exception=True)  # 65번에서 설정해준 serializer 를 요청받은 data 와 serializers.py안에 있는 LoginSerializer 데이터와 서로 비교하여 유효성검사

        return Response(serializer.data, status=status.HTTP_200_OK)