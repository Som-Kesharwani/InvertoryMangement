from rest_framework import serializers
from . import models
from Product.models import Product

class SalesSerializer(serializers.HyperlinkedModelSerializer):
    product_id = serializers.CharField(max_length=50)
    class Meta:
        model = models.Sales
        fields = ("product_id", "quantity_sold")
    def create(self, validated_data):
        product_id = validated_data.pop("product_id")
        product_id = Product.objects.get(SKU=product_id)
        inventory = models.Inventory.objects.get_or_create(product=product_id)[0]
        inventory.quantity_available -= validated_data.get("quantity_sold")
        inventory.save()
        return models.Sales.objects.create(product=product_id, **validated_data)

class PurchaseSerialiser(serializers.HyperlinkedModelSerializer):
    product_id = serializers.CharField(max_length=50)
    class Meta:
        model = models.Purchase
        fields = ("product_id","quantity_purchased")
    def create(self, validated_data):
        product_id = validated_data.pop("product_id")
        product_id = Product.objects.get(SKU=product_id)
        inventory = models.Inventory.objects.get_or_create(product=product_id)[0]
        inventory.quantity_available += validated_data.get("quantity_purchased")
        inventory.save()
        return models.Purchase.objects.create(product=product_id, **validated_data)
