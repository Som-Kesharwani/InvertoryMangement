from django.db import models
from django.conf import settings
import uuid



def setDefault():
    return ProductCategory.objects.get_or_create(name='default', type="Generic")

def get_sentinel_category():
    return ProductCategory().objects.get_or_create(name="Default",parentCategory="Default")[0]

# Create your models here.
class ProductCategory(models.Model):
    #Here we going to store the product category and subcategory
    def __str__(self) -> str:
        return self.name
    choices =  (('Generic', 'Generic'), ('Specific', 'Specific'))
    level = models.IntegerField(default=1)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=15,choices=choices,blank=False,null=False,default='Generic')
    parentCategory = models.ForeignKey(to = "ProductCategory",on_delete=models.SET_DEFAULT, default=setDefault)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    SKU = models.UUIDField(primary_key=True, default=uuid.uuid4, editable = False)
    created_at = models.DateTimeField(auto_now=True,)
    modified_st = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("ProductCategory",on_delete=models.SET_DEFAULT, default=setDefault)
