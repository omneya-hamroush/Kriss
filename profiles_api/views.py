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
from django.db.models import Q
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework import permissions
from django.test.client import Client

from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.ProductSerializer
    queryset=models.Product.objects.all()
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('name',)
    search_fields = ('name',)
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        queryset = models.Product.objects.all()
        latest = self.request.query_params.get('latest')
        best_seller = self.request.query_params.get('best_seller')
        if latest:
            queryset = queryset.filter(latest=latest)
        elif best_seller:
            queryset = queryset.filter(best_seller=best_seller)
            return queryset


    # def get_queryset(self):
    #     queryset = super(ProductViewSet, self).get_queryset().filter(
    #         in_stock=True
    #     )
    #     query_params = self.request.query_params
    #     query = Q()
    #     search = query_params.get('search')
    #     if search:
    #         query.add(Q(name__icontains=search), Q.AND)
    #
    #     # ........ mack pro filters .......
    #     if query_params.get('macbookpro') == 'true':
    #         queryset = queryset.filter(subcategory__name='MacBook Pro')
    #     if query_params.get('15inch') == 'true':
    #         queryset = queryset.filter(subcategory__name='15inch')
    #     if query_params.get('13inch') == 'true':
    #         queryset = queryset.filter(subcategory__name='13inch')
    #     # ........ filters .......
    #     if query_params.get('subcategory_id'):
    #         query.add(
    #             Q(subcategory__id=query_params.get('subcategory_id')), Q.AND)
    #
    #     if query_params.get('price_low'):
    #         query.add(
    #             Q(
    #                 price__gte=query_params.get('price_low'),
    #                 productproperties__isnull=True
    #             ) |
    #             Q(
    #                 productproperties__price__gte=query_params.get(
    #                     'price_low'),
    #                 productproperties__isnull=False
    #             ),
    #             Q.AND
    #         )
    #     if query_params.get('price_heigh'):
    #         query.add(
    #             Q(
    #                 price__lte=query_params.get('price_heigh'),
    #                 productproperties__isnull=True
    #             ) |
    #             Q(
    #                 productproperties__price__lte=query_params.get(
    #                     'price_heigh'),
    #                 productproperties__isnull=False
    #             ),
    #             Q.AND
    #         )
    #     if query_params.get('brand_id'):
    #         query.add(Q(brand__id=query_params.get('brand_id')), Q.AND)
    #
    #     queryset = queryset.filter(query)
    #
    #     # ........ sort .......
    #     if query_params.get('sort'):
    #         queryset = queryset.order_by(query_params.get('sort'))
    #
    #     return queryset






    # def add_to_cart(self, request, pk=None):
    #     product= self.get_object()
    #     serializer= serializers.ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         if request.method == 'PUT':
    #             product.add_to_cart(serializer.data['product'])
    #             product.save()
    #             return Response({'status': 'product added'})
    #         else:
    #             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





    # @action(detail=True, methods=['put'],url_path="add_to_cart", url_name="add_to_cart")
    # def add_to_cart(self, request, pk= None):
    #     product=self.get_object()
    #     serializer=serializers.ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         print("i am in if")
    #         product.add_to_cart(serializer.data['product'])
    #         product.save()
    #         return Response({'status': 'product added'})
    #     else:
    #         print("i am on else")
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)


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



class CartViewSet (viewsets.ModelViewSet):
    serializer_class=serializers.CartSerializer
    queryset=models.Cart.objects.all()
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = [permissions.IsAdminUser]






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


# def add_to_cart (self,request):
#     product= Product.objects.get(pk=int(request.GET['product_id']))
