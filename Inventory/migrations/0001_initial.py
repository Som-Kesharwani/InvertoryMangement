# Generated by Django 4.2.6 on 2023-11-11 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Product", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sales",
            fields=[
                ("sale_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("quantity_sold", models.IntegerField()),
                ("sale_date", models.DateTimeField(auto_now=True)),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="Product.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Puschase",
            fields=[
                ("purchase_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("quantity_purchased", models.IntegerField()),
                ("purchase_date", models.DateTimeField(auto_now=True)),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="Product.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "inventory_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("quantity_available", models.IntegerField()),
                ("create_date", models.DateTimeField(auto_now=True)),
                ("update_date", models.DateTimeField(auto_now_add=True)),
                (
                    "product_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="Product.product",
                    ),
                ),
            ],
        ),
    ]
