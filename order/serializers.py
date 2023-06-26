from dataclasses import field
from rest_framework import serializers
from .models import Order, OrderItem
# from .cart import Cart
#
#
# class OrderItemsSerializer(serializers.ModelSerializer) :
#     class Meta :
#         model = OrderItem
#         fields = "__all__"
#
#
# class OrderSerializer(serializers.ModelSerializer) :
#     orderItems = serializers.SerializerMethodField(method_name = 'get_order_items', read_only = True)
#
#     class Meta :
#         model = Order
#         fields = "__all__"
#
#     def get_order_items(self, obj) :
#         order_items = obj.orderitems.all()
#         serializer = OrderItemsSerializer(order_items, many = True)
#         return serializer.data
#
#
# class CartSerializer(serializers.ModelSerializer) :
#     class Meta :
#         model = Cart
#         fields = '__all__'
#
#
# class CartAddSerialzer(serializers.Serializer) :
#     quantity = serializers.IntegerField(min_value = 1, max_value = 9)
#
# class CouponApplySerialzer(serializers.Serializer) :
# 	code = serializers.CharField()

from dataclasses import field
from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):

    orderItems = serializers.SerializerMethodField(method_name='get_order_items', read_only=True)

    class Meta:
        model = Order
        fields = "__all__"

    def get_order_items(self, obj):
        order_items = obj.orderitems.all()
        serializer = OrderItemsSerializer(order_items, many=True)
        return serializer.data