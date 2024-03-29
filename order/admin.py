from django.contrib import admin
from .models import Order, Coupon,OrderItem



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'updated', 'paid')
	list_filter = ('paid',)
	


admin.site.register(Coupon)
admin.site.register(OrderItem)