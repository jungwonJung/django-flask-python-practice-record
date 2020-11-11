from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt   # 보안관련
from rest_framework.parsers import JSONParser

from .models import Addresses
from .serializers import AddressesSerializer

@csrf_exempt   # csrf forbidden 에러 해결
def address_list(request):       # HTTP    request = 호출 ,,,,response = 응답
    if request.method == 'GET':
        queryset = Addresses.objects.all()
        serializer = AddressesSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def address(request, pk):

    obj = Addresses.objects.get(pk=pk)  # 단건조회

    if request.method == 'GET':
        queryset = Addresses.objects.all()
        serializer = AddressesSerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AddressesSerializer(obj, data=data)   # 'PUT' 에는 모델명이들어가야함 객체와 모델명
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)   # DELETE는 HttpResponse




