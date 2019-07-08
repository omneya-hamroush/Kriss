from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from profiles_api import serializers, permissions, authentication
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
#from profiles_api import permissions
# from services.email_helper import send_email
from rest_framework import filters
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
#from django.db.models import Q
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import permissions
from django.test.client import Client

from django_filters.rest_framework import DjangoFilterBackend


class FamilyViewSet (viewsets.ModelViewSet):
    serializer_class= serializers.FamilySerializer
    queryset= models.Family.objects.all()
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = models.Family.objects.all()
        query_params = self.request.query_params
        brand= self.request.query_params.get('brand', None)

        if brand is not None:
            queryset=queryset.filter(brands__brand_name=brand)
            return queryset



class ProductViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.ProductSerializer
    queryset=models.Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('name',)
    search_fields = ('name',)
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #IsAdminUser
    #filteration
    def get_queryset(self):
        queryset = models.Product.objects.all()
        query_params = self.request.query_params
        latest = self.request.query_params.get('latest', None)
        best_seller= self.request.query_params.get('best_seller',None)
        if latest is not None:
            queryset = queryset.filter(latest=True)
        if best_seller is not None:
            queryset = queryset.filter(best_seller=True)
        return queryset


    def get_queryset(self):
        queryset = models.Product.objects.all()
        query_params = self.request.query_params
        product= self.request.query_params.get('product', None)

        for i in ['category', 'family__brands',]:
            filter = self.request.query_params.get(i, None)
            if filter is not None:
                queryset=queryset.filter(
                    **{i:filter}
                )
        if product is not None:
            queryset=queryset.filter(name__icontains=product)
            # queryset=queryset.filter(category=category)
            # queryset=queryset.filter(family__brands=brand)
        return queryset



class PictureViewSet (viewsets.ModelViewSet):
    serializer_class = serializers.PictureSerializer
    queryset=models.Picture.objects.all()
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class CartViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.CartSerializer
    queryset=models.Cart.objects.all()
    #append
    def put (self,request):
        queryset=models.Cart.objects.all()
        query_params = self.request.query_params
        for i in['cart__id',]:
            add_to_cart= self.request.query_params.get(i, None)
            if add_to_cart is not None:
                queryset=queryset.append()



class StoreViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.StoreSerializer
    queryset=models.Store.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('store_area', 'store_city',)
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ContactUsViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.ContactUsSerializer
    queryset=models.ContactUs.objects.all()
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [permissions.IsAdminUser]
    # def send_comment (self, request, pk=None):
    #     contact_us=self.get_object()


    # @action(detail=True, methods=['post'])
    # def send_comment(self, request, pk=None):
    #     contact_us = self.get_object()
    #     serializer = ContactUsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         print ("in if")
    #         contact_us.send_comment(serializer.data['contact us'])
    #         contact_us.save()
    #         return Response({'status': 'comment sent'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)

    # def send_message (self,request):
    #     if request.method=='POST':
    #         serializer = ContactUsSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({'data':serializer.data})
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def send_comment(self, request):
    #     form=UserMessageForm(request.POST)
    #     if form.is_valid():
    #         text=form.cleaned_data
    #
    #     return Response ({'data':text.data})

    # def create (self, request):
    #     subject = 'New subject'
    #     # data=request.data
    #     form_subject= models.ContactUs.objects.create(
    #     client_name=request.data.get('client_name'),
    #     client_email=request.data.get('client_email'),
    #     subject=request.data.get('subject'),
    #     how_can_i_help= request.data.get('how_can_i_help')
    #
    #     )
    #     form_subject.save()
    #     message = "client_name: %s<br>client_email: %s<br>subject: %s<br>how_can_i_help: %s" % (
    #         form_subject.client_name,
    #         form_subject.client_email,
    #         form_subject.subject,
    #         form_subject.how_can_i_help
    #     )
    #     subject = '%s: %s #%d: %s' % (
    #         subject,
    #         form_subject.client_name,
    #         form_subject.client_email,
    #         form_subject.id
    #     )
    #     send_email(
    #         message=message,
    #         subject=subject,
    #         recipients=['omnia.hamroush@student.guc.edu.eg']
    #     )
    #     return Response("Thanks, your comment has been sent")
    #


class AboutUsViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.AboutUsSerializer
    queryset=models.AboutUs.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class BrandViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.BrandSerializer
    queryset=models.Brand.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [permissions.IsAdminUser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category_name',)

    def get_queryset(self):
        queryset = models.Category.objects.all()
        query_params = self.request.query_params
        category= self.request.query_params.get('category', None)

        if category is not None:
            queryset=queryset.filter(category_name=category)
            return queryset



class CartItemViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.CartItemSerializer
    queryset=models.CartItem.objects.all()

    def create(self, request):
        serializer= serializers.CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # cart= models.Cart.objects.get(pk=int(request.GET['cart_id']))
            # product= models.Product.objects.get(pk=int(request.GET['product_id']))
            # cart=serializer.validated_data.get('cart')
            # product=serializer.validated_data.get('product')
            #message= f'new cart item {cart, product}!'
            return Response ({'data':serializer.data})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )




class LatestOfferViewSet (viewsets.ModelViewSet):
    serializer_class= serializers.LatestOfferSerializer
    queryset=models.LatestOffer.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderViewSet (viewsets.ModelViewSet):
    serializer_class= serializers.OrderSerializer
    queryset= models.Order.objects.all()
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [permissions.NoPermission]
