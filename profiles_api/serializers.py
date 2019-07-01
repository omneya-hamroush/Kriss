from rest_framework import serializers
from profiles_api import models



class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'description',
            'price',
            'product_image',
        )
        model = models.Product
    def create(self, validated_data):

        product = models.Product.objects.create_product(

            name=validated_data['name'],
            description=validated_data['description'],
            price=validated_data['price'],
            product_image=validate_data['product_image'],
        )

        return product


class ShopPageSerializer (serializers.ModelSerializer):
    class Meta:
        fields = (
        'product',
        'instructions',
        'ingredients',
        )
        model = models.ShopPage


class PictureSerializer (serializers.ModelSerializer):
    class Meta:
        fields = (
        'title',
        'subtitle',
        'gallerie',
        )
        model = models.Picture


class AboutUSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'client_name',
        'client_email',
        'subject',
        'how_can_i_help',
        'working_hours',
        )
        model = models.AboutU


class StoreSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'area',
        'city',
        )
        model= models.Store


class BrandSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'brand_name',
        'is_featured',
        )
        model=models.Brand


class CategorieSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'category_name',
        'brands',
        )
        model=models.Categorie


class CartSerializer (serializers.ModelSerializer):
    class Meta:
        fields=(
        'total_price',
        'number_of_products',
        )
        model=models.Cart
