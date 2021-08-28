from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from Users.serializers import Sdesgin_UsersSerializer
from Users.models import Sdesgin_Users


class Sdesgin_UsersViewSet(ViewSet):

    def list(self, request):
        queryset = Sdesgin_Users.objects.order_by('pk')
        serializer = Sdesgin_UsersSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = Sdesgin_UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Sdesgin_Users.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = Sdesgin_UsersSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Sdesgin_Users.objects.get(pk=pk)
        except Sdesgin_Users.DoesNotExist:
            return Response(status=404)
        serializer = Sdesgin_UsersSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Sdesgin_Users.objects.get(pk=pk)
        except Sdesgin_Users.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
