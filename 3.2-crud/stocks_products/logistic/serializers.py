from pyexpat import model
from rest_framework import serializers
from .models import Product, Stock, StockProduct
from .filters import ProductsFilter

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__' 


class ProductPositionSerializer(serializers.ModelSerializer):

     class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id','address', 'products','positions']
        filter_class = ProductsFilter


    def create(self, validated_data):

        positions = validated_data.pop('positions')
        stock = super().create(validated_data)

        for product in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=product['product'],
                quantity=product['quantity'],
                price=product['price']
            )

        return stock

    def update(self, instance, validated_data):

        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)

        for product in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=product['product'],
                defaults={
                'quantity': product['quantity'],
                'price': product['price']
                }
            )

        return stock
