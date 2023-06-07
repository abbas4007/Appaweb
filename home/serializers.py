from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from bucket import bucket
from .models import Product
class BucketHomeSerializer(serializers.Serializer):
    class Meta:

        model =Product
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        model =Product
        fields = '__all__'