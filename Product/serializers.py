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
    def create(self, validated_data):
        return Category.objects.create(level=1,**validated_data)

class SubCategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(max_length=20)
    class Meta:
        model = SubCategory
        fields = ( "name", "type","category")
    def create(self, validated_data):
        cat = validated_data.get("category")
        cat= Category.objects.filter(name=cat)
        validated_data.pop("category")
        return SubCategory.objects.create(**validated_data)
 
    
class ProductSerializer(serializers.HyperlinkedModelSerializer):
        subCategory = serializers.CharField(max_length=10)
        class Meta:
            model = Product
            fields = ('name','description', 'subCategory')
        
        def create(self, validated_data):
            sub = validated_data.get("subCategory")
            sub= Category.objects.get(name=sub)
            validated_data.pop("subCategory")
            level = 1
            return Product.objects.create(subCategory=sub, **validated_data)
   

