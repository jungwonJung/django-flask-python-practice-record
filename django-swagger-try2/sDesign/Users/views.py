from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Sdesign_Users
from .serializers import Sdesgin_UsersSerializer
# Create your views here.

# 클래스형 viwe 안에 함수형 변수 생성

class Users(GenericAPIView):

    serializer_class = Sdesgin_UsersSerializer
    def get(self, request):

        objects = Sdesign_Users.objects.all()
        serializer = Sdesgin_UsersSerializer(objects, many=True)
        return Response(serializer.data)

        
    def post(self, request):

        data = request.data

        obj = Sdesign_Users.objects.create(username=data['username'],userpw=['userpw'],useremail=['useremail'])
        return HttpResponse("생성되었습니다")

class Login(GenericAPIView):

    serializer_class = Sdesgin_UsersSerializer
    def get(self, request):

        