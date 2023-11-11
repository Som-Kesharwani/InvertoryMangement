from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Category, Product, SubCategory

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','email', 'username']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ( "name", "type")

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubCategory
        fields = ( "name", "type")
 
    
class ProductSerializer(serializers.HyperlinkedModelSerializer):
        category = serializers.CharField(max_length=10)
        subCategory = serializers.CharField(max_length=10)
        class Meta:
            model = Product
            fields = ('name','description','category', 'subCategory')
        
        def create(self, validated_data):
            cat = validated_data.get("category")
            cat= Category.objects.get(name=cat)
            sub = validated_data.get("subCategory")
            sub= Category.objects.get(name=sub)
            validated_data.pop("subCategory")
            validated_data.pop("category")
            return Product.objects.create(category=cat,subCategory=sub, **validated_data)
   

