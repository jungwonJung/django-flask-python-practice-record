from django.shortcuts import render
from rest_framework import generics, status, views
from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
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
from .renderes import UserRenderer
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util


# Create your views here.
class RegisterView(generics.GenericAPIView):
   
    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer, )

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



class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer =self.serializer_class(data=request.data)

        email = request.data['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request = request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64' : uidb64,'token' : token})
            absurl = 'http://' + current_site +  relativeLink
            email_body = 'hi, /n 링크를 비밀번호를 재설정 하세요 /n'+ absurl
            data = {'email_body' : email_body, 'to_email' : user.email, 
                    'email_subject' : '비밀번호를 재설정 하세요!!'}

            Util.send_email(data)
        return Response({'success': '비밀번호를 재설정 할 수 있는 링크를 이메일로 보내겠습니다!'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id = id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error' : '토큰이 유효하지 않습니다. 새 토큰을 요청하십시오.'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'success' : True, 'message' : '인증된 계정입니다','uidb64' : uidb64, 'token' : token}, status=status.HTTP_200_OK)

            
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error' : '토큰이 유효하지 않습니다. 새 토큰을 요청하십시오.'}, status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success' : True, 'message' : '비밀번호가 성곡적으로 변경되었습니다'}, status=status.HTTP_200_OK)