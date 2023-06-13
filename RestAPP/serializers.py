from rest_framework import serializers
from RestAPP.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'pname', 'category', 'price', 'supplier', 'supplierid']