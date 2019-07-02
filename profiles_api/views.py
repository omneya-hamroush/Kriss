from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
#from profiles_api import permissions
from rest_framework import filters
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.ProductSerializer
    queryset=models.Product.objects.all()
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('name',)
    # search_fields = ('name',)
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAdminUser]



class ShopPageViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.ShopPageSerializer
    queryset=models.ShopPage.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAdminUser]

    @action(detail=True, methods=['put'],url_path="add_to_cart", url_name="add_to_cart")
    def add_to_cart(self, request, pk= None):
        product=self.get_object()
        serializer=serializers.ProductSerializer(data=request.data)
        if serializer.is_valid():
            print("i am in if")
            product.add_to_cart(serializer.data['product'])
            product.save()
            return Response({'status': 'product added'})
        else:
            print("i am on else")
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    # def list(self, request):
    #     queryset = ShopPage.objects.all()
    #     serializer = ShopPageSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = ShopPage.objects.all()
    #     shop_page = get_object_or_404(queryset, pk=pk)
    #     serializer = ShopPageSerializer(shop_page)
    #     return Response(serializer.data)



class PictureViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.PictureSerializer
    queryset=models.Picture.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAdminUser]




class GalleryViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.GallerySerializer
    queryset=models.Gallery.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAdminUser]



class CartViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.CartSerializer
    queryset=models.Cart.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, pk=None):

    # def list(self, request):
    #     queryset = Cart.objects.all()
    #     serializer = CartSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, pk=None):
    #     queryset = Cart.objects.all()
    #     cart = get_object_or_404(queryset, pk=pk)
    #     serializer = CartSerializer(cart)
    #     return Response(serializer.data)


class StoreViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.StoreSerializer
    queryset=models.Store.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('store_area', 'store_city',)
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAdminUser]


class ContactUsViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.ContactUsSerializer
    queryset=models.ContactUs.objects.all()
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [permissions.IsAdminUser]

    @action(detail=True, methods=['post'])
    def send_comment(self, request, pk=None):
        contact_us = self.get_object()
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            print ("in if")
            contact_us.send_comment(serializer.data['contact us'])
            contact_us.save()
            return Response({'status': 'comment sent'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)



class AboutUsViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.AboutUsSerializer
    queryset=models.AboutUs.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAdminUser]



class BrandViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.BrandSerializer
    queryset=models.Brand.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAdminUser]
    #filter_backends = (filters.SearchFilter,)
    #search_fields = ('brand_name',)
    # def list (self, request):
    #     brand_id=request.params.get()
    #     try:
    #         brand= models.Brand.objects.get(id=brand_id)
    #     # except:
	# 	# 	return Response({serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #     product= models.Product.objects.filter(brand=brand)
    #     serializer = serializers.ProductSerializer(product, many =True)
    #     return Response({
	#             'status': '200',
	#             'data': serializer.data},
    #         	status = status.HTTP_200_OK)



class CategoryViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.CategorySerializer
    queryset=models.Category.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category_name',)
