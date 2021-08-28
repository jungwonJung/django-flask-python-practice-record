from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# ListCreateAPIView :
# 모델 인스턴스 컬렉션 을 나타내는 읽기-쓰기 엔드 포인트에 사용됩니다 .
# get및 post메서드 처리기를 제공합니다 .
# 확장 : GenericAPIView , ListModelMixin , CreateModelMixin

# RetrieveUpdateAPIView :
# 단일 모델 인스턴스 를 나타내는 읽기 또는 업데이트 엔드 포인트에 사용됩니다 .
# 제공 get, put및 patch방법 핸들러.
# 확장 : GenericAPIView , RetrieveModelMixin , UpdateModelMixin
from .serializers import IncomeSerializer
from .models import Income
from rest_framework import permissions
from .permissions import IsOwner


class IncomeListAPIView(ListCreateAPIView): # ListCreateAPIView   GET, POST API 기능 생성
    serializer_class = IncomeSerializer # 사용할 직렬화 class 설정 
    query_set = Income.objects.all()  # .models.py 에서 Expense class 의 저장된 objects 전부를 query_set 으로 지정한다
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
    # perform_create()은 create()의 동작 중 일부분을 overriding한다고 생각하면 되는데, serializer.save()가 호출될 때 
    # perform_create()가 호출된다고 생각하면 된다. 위의 경우 명시적으로 perform_create()를 호출했지만, 
    # django에서는 개발자의 짐을 덜어주기위해 mixin으로 앞에서 설명한 list(), create()등을 제공하는 데, 이때 자동으로 save()대신 perform_create()를 호출하는 것이다. 
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.query_set.filter(owner=self.request.user)

class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):   # RetrieveUpdateAPIView 를 사용하면 mixin 과 비슷한기능으로 GET, PUT,PATCH , DELETE 기능 생성
    serializer_class = IncomeSerializer
    query_set = Income.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    lookup_field = "id"  # swagger try out 시 field placeholder 설정

    def get_queryset(self):
        return self.query_set.filter(owner=self.request.user)