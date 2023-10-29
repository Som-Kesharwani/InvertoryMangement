# Generated by Django 4.2.6 on 2023-10-29 13:32

import Product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "parentCategory",
                    models.ForeignKey(
                        null=True,
                        on_delete=models.SET(Product.models.get_sentinel_category_id),
                        to="Product.productcategory",
                    ),
                ),
            ],
        ),
    ]
