from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from profiles_api import serializers

class ProductViewSet (viewsets.ViewSet):
    serializers_class= serializers.ProductSerializer

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self,request):
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message= f'New product {name}!'
            return Response ({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk= None):
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk= None):
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk= None):
        return Response({'http_method':'DELETE'})            
