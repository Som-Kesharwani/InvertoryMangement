from django.db import models
from django.conf import settings
import uuid 

#to do
# create category and subcategory 
# this will help in partitioning and bucketing the data and increase the efficiency of the code.

def get_sentinel_category():
    return Category().objects.get_or_create(name="Default",parentCategory="Default",level=0)[0]

# Create your models here.
class Category(models.Model):
    #Here we going to store the product category and subcategory
    def __str__(self) -> str:
        return self.name
    choices =  (('Generic', 'Generic'), ('Specific', 'Specific'))
    level = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=15,choices=choices,blank=False,null=False,default=3)
  
class SubCategory(models.Model):
    def __str__(self) -> str:
        return self.name
    choices =  (('Generic', 'Generic'), ('Specific', 'Specific'))
    level = models.IntegerField()
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=15,choices=choices,blank=False,null=False,default=3)



class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    SKU = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    created_at = models.DateTimeField(auto_now=True,)
    modified_st = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category",on_delete=models.CASCADE)
    subCategory = models.ForeignKey("SubCategory",on_delete=models.CASCADE)