from rest_framework import serializers
from profiles_api import models



class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'description',
            'price',
        )
        model = models.Product
    def create(self, validated_data):

        product = models.Product.objects.create_product(

            name=validated_data['name'],
            description=validated_data['description'],
            price=validated_data['price']
        )

        return product
