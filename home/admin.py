from django.contrib import admin
from .models import Category, Product,Lesson


admin.site.register(Category)
admin.site.register(Lesson)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	raw_id_fields = ('category',)