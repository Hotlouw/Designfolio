

from rest_framework import serializers
from .models import Product,CartItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'details', 'category','cost','price','supplier']

    def create(self, validated_data):
        """
        Create and return a new `shop` instance, given the validated data.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `shop` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.image = validated_data.get('image', instance.image)
        instance.details = validated_data.get('details', instance.details)
        instance.category = validated_data.get('category', instance.category)
        instance.cost = validated_data.get('cost', instance.cost)
        instance.price = validated_data.get('price',instance.price)
        instance.supplier = validated_data.get('supplier',instance.supplier)
        instance.save()
        return instance
    

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'name', 'image', 'details', 'category','cost','price','supplier']