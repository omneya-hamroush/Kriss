from rest_framework import serializers
from rest_framework import pagination
from profiles_api import models
from django.core.paginator import Paginator
# from rest_framework.pagination import PaginationSerializer


class ProductSerializer (serializers.ModelSerializer):
    # next = pagination.NextPageField(source='*')
    # prev = pagination.PreviousPageField(source='*')

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'price',
            'in_stock',
            'product_image',
            'family',
            'latest',
            'best_seller',
            'instructions',
            'ingredients',
            'category',
            'short_line_1',
            'short_line_2',
            'short_line_3',

        )
        model = models.Product


# class CustomPaginationSerializer(pagination.BasePaginationSerializer):
#     links = LinksSerializer(source='*')
#     total_results = serializers.Field(source='paginator.count')
#
#     results_field = 'objects'

# class PaginatedProductSerializer(pagination.PaginationSerializer):
#
#     class Meta:
#         object_serializer_class = ProductSerializer
#


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
        'id',
        'client_name',
        'client_email',
        'subject',
        'how_can_i_help',

        )
        model= models.ContactUs






class PictureSerializer (serializers.ModelSerializer):
    #picture = serializers.SerializerMethodField()
    class Meta:
        fields = (
        'id',
        'title',
        'subtitle',
        'picture_upload',
        'action_button',
        )
        model = models.Picture
        # def get_picture(self, obj):
        #     picture = obj.picture
        #     if not picture:
        #        return None
        #     return {
        #        "id": picture.id,
        #        "title": picture.title,
        #        "subtitle":picture.subtitle,
        #        "picture_upload":picture.picture_upload,
        #        "action_button":picture.action_button
        #         }




class AboutUsSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'about',
        'get_to_know_us',
        )
        model = models.AboutUs


class StoreSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'id',
        'store_area',
        'store_city',
        'location_longitude',
        'location_latitude',

        )
        model= models.Store


class BrandSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'id',
        'brand_name',
        'is_featured',
        )
        model=models.Brand


class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'id',
        'category_name',

        )
        model=models.Category


class CartSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'id',
        'total_price',
        'number_of_products',
        'products',
        )
        model=models.Cart


class CartItemSerializer (serializers.ModelSerializer):
    cart = serializers.CharField(required=False)
    class Meta:
        fields=(
        'id',
        'cart',
        'product',
        'quantity',

        )
        model=models.CartItem


class FamilySerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'id',
        'family_name',
        'brand',
        'is_featured',
        )
        model=models.Family


class LatestOfferSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'offer_link',
        'offer_width',
        'offer_image',
        'image_text',
        )
        model=models.LatestOffer


class OrderSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        '__all__'
        )
        model=models.Order
