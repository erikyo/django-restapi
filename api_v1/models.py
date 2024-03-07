from django.db import models
from rest_framework import serializers


# Category model
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'


class CategoryInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


# Product model
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'


class ProductInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)



