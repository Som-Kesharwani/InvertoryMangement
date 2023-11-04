from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ProductCategory

class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','email', 'username']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    parentCategory = serializers.CharField(max_length=10)
    class Meta:
        model = ProductCategory
        fields = '__all__'
    #parentCategory = serializers.PrimaryKeyRelatedField(allow_blank=True)
    def create(self, validated_data):
        parentCategory = validated_data.get("parentCategory", None)
        validated_data.pop("parentCategory")
        print("Datav 121", parentCategory)
        if parentCategory == None or parentCategory == "Default":
            cat = ProductCategory.objects.get_or_create(name = "Default",type="Generic")[0]
        else:
            cat = ProductCategory.objects.filter(name=parentCategory)[0]

        #prod = ProductCategory.objects.get_or_create(name, type, obj)
        return ProductCategory.objects.create(parentCategory=cat, **validated_data)
   

