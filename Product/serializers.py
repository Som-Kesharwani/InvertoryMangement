from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ProductCategory, Product

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','email', 'username']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    parentCategory = serializers.CharField(max_length=20, required=False)
    class Meta:
        model = ProductCategory
        fields = ('name', 'type','parentCategory')
    #parentCategory = serializers.PrimaryKeyRelatedField(allow_blank=True)
    def create(self, validated_data):
        parentCategory = validated_data.get("parentCategory", None)
        validated_data.pop("parentCategory")
        if parentCategory == None or parentCategory == "default":
            parentCategory = ProductCategory.objects.get_or_create(name = "default",type="Generic",parentCategory=None)[0]
        else:
            parentCategory = ProductCategory.objects.filter(name=parentCategory)[0]
        print("Error : This is cat ",parentCategory)
        level = parentCategory.level + 1
        #prod = ProductCategory.objects.get_or_create(name, type, obj)
        return ProductCategory.objects.create(level=level ,parentCategory=parentCategory, **validated_data)
   
class ProductSerializer(serializers.HyperlinkedModelSerializer):
        category = serializers.CharField(max_length=20, required=False)
        class Meta:
            model = Product
            fields = ('name','brand','description', 'category')
        
        def create(self, validated_data):
            category = validated_data.get("category",None)
            if category==None or category == '' or category == 'default':
                category= ProductCategory.objects.get_or_create(name='default')
            else:
                category= ProductCategory.objects.filter(name=category)[0]
            validated_data.pop("category")
            return Product.objects.create(category=category, **validated_data)
   
