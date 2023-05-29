from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from bucket import bucket

class BucketHomeSerializer(serializers.Serializer):
    url = serializers.URLField(bucket.u)
