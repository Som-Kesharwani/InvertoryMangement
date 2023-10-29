from django.db import models
from django.conf import settings



def get_sentinel_category():
    return ProductCategory().objects.get_or_create(name="Default",parentCategory="Default")[0]

def get_sentinel_category_id():
    return get_sentinel_category().id
# Create your models here.
class ProductCategory(models.Model):
    #Here we going to store the product category and subcategory
    name = models.CharField(max_length=50)
    parentCategory = models.ForeignKey(to = "ProductCategory",on_delete=models.SET(get_sentinel_category_id),null=True)
