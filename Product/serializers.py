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
    #parentCategory = serializers.PrimaryKeyRelatedField(allow_blank=True)
    class Meta:
        model = ProductCategory
        fields = ('name','parentCategory')
    def create(self, validated_data):
        category = validated_data.get('parentCategory')
        print("This is new logs 5161: ",category)
        if category == None:
            cat = ProductCategory.objects.get_or_create(name="default")[0]
            category = cat

        post = ProductCategory(
                name = validated_data['name'],
                parentCategory = category
        )
        post.save()
        return post
   

