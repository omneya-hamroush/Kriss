from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
#from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated


class ProductViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.ProductSerializer
    queryset=models.Product.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

# class ProductViewSet (viewsets.ViewSet):
#     serializer_class= serializers.ProductSerializer
#
#     def list(self, request):
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Product.objects.all()
#         product = get_object_or_404(queryset, pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def create(self,request):
#         serializer= self.serializer_class(data=request.data)
#
#         if serializer.is_valid():
#             name=serializer.validated_data.get('name')
#             message= f'New product {name}!'
#             return Response ({'message':message})
#         else:
#             return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#             )
#
#     def update(self, request, pk= None):
#         return Response({'http_method':'PUT'})
#
#     def partial_update(self, request, pk= None):
#         return Response({'http_method':'PATCH'})
#
#     def destroy(self, request, pk= None):
#         return Response({'http_method':'DELETE'})

    # def search(request):
    #     if request.method == 'GET':
    #         product_name =  request.GET.get('search')
    #     try:
    #         status = Add_prod.objects.filter(Product_name=product_name)
    #         return render(request,"",{"products":status})
    #     else:
    #         return render(request,"",{})


class ShopPageViewSet (viewsets.ViewSet):
    serializer_class=serializers.ShopPageSerializer

    def list(self, request):
        queryset = ShopPage.objects.all()
        serializer = ShopPageSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ShopPage.objects.all()
        shop_page = get_object_or_404(queryset, pk=pk)
        serializer = ShopPageSerializer(shop_page)
        return Response(serializer.data)



class PictureViewSet (viewsets.ViewSet):
    serializer_class = serializers.PictureSerializer

    def list(self, request):
        queryset = Picture.objects.all()
        serializer = PictureSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Picture.objects.all()
        picture = get_object_or_404(queryset, pk=pk)
        serializer = PictureSerializer(picture)
        return Response(serializer.data)


    def create(self,request):
        serializer= self.serializer_class(data=request.data)

        if serializer.is_valid():
            title=serializer.validated_data.get('name')
            message= f'New product {name}!'
            return Response ({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

class CartViewSet (viewsets.ViewSet):
    serializer_class=serializers.CartSerializer


    def list(self, request):
        queryset = Cart.objects.all()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cart.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
