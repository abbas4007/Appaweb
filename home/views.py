from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product, Category
# from . import tasks
from django.contrib import messages
# from utils import IsAdminUserMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BucketHomeSerializer
from order.forms import CartAddForm
from .forms import PostSearchForm

class HomeView(View):
	form_class = PostSearchForm
	def get(self, request, category_slug=None) :
		products = Product.objects.filter(available = True)
		categories = Category.objects.filter(is_sub = False)
		products = Product.objects.all()
		if request.GET.get('search') :
			products = products.filter(name__contains = request.GET['search'])
		if category_slug :
			category = Category.objects.get(slug = category_slug)
			products = products.filter(category = category)
		return render(request, 'home/index.html', {'products' : products, 'categories' : categories,'form':self.form_class})

class BucketHome(APIView):
	def get(self, request, category_slug=None) :
		products = Product.objects.filter(available = True)
		categories = Category.objects.filter(is_sub = False)
		if category_slug :
			category = Category.objects.get(slug = category_slug)
			products = products.filter(category = category)
		products_ser =BucketHomeSerializer(products,many = True)
		return Response(products_ser.data, status = status.HTTP_200_OK)

class ProductDetailView(View):
	def get(self, request, slug):
		product = get_object_or_404(Product, slug=slug)
		form = CartAddForm()
		return render(request, 'home/detail.html', {'product':product, 'form':form})

# class BucketHomeApi(IsAdminUserMixin, View):
# 	template_name = 'home/bucket.html'
#
# 	def get(self, request):
# 		objects = tasks.all_bucket_objects_task()
# 		return render(request, self.template_name, {'objects':objects})

# class BucketHomeApi(APIView):
# 	def get(self, request):
# 		objects = tasks.all_bucket_objects_task()
# 		obj = BucketHomeSerializer(objects,many = True)
# 		return Response (obj.data,status = status.HTTP_200_OK)
#
#
# class DeleteBucketObject(IsAdminUserMixin, View):
# 	def get(self, request, key):
# 		tasks.delete_object_task.delay(key)
# 		messages.success(request, 'your object will be delete soon.', 'info')
# 		return redirect('home:bucket')
#
# class DeleteBucketObjectApi(APIView):
# 	def get(self, request, key):
# 		tasks.delete_object_task.delay(key)
# 		return Response(request, status.HTTP_200_OK)
#
# class DownloadBucketObject(IsAdminUserMixin, View):
# 	def get(self, request, key):
# 		tasks.download_object_task.delay(key)
# 		messages.success(request, 'your download will start soon.', 'info')
# 		return redirect('home:bucket')
#
# class DownloadBucketObjectApi(APIView):
# 	def get(self, request, key):
# 		tasks.download_object_task.delay(key)
# 		return Response(request, status.HTTP_200_OK)