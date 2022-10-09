# Generated by Django 4.1.1 on 2022-09-30 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(default="", max_length=50),
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(default="", upload_to="shop/images"),
        ),
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="sub_category",
            field=models.CharField(default="", max_length=50),
        ),
    ]
