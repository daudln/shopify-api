# Generated by Django 4.2.2 on 2023-07-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_alter_productimage_image"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="cartitem",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="cartitem",
            constraint=models.UniqueConstraint(
                fields=("cart", "product"), name="unique_product_cart"
            ),
        ),
    ]
