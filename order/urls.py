from django.urls import path
from . import views



app_name = 'order'
urlpatterns = [
	path('create/', views.OrderCreateView.as_view(), name='order_create'),
	path('create/', views.OrderCreateApiView.as_view(), name='order_create_api'),
	path('detail/<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
	path('detail/<int:order_id>/', views.OrderDetailApiView.as_view(), name='order_detail_api'),
	path('cart/', views.CartView.as_view(), name='cart'),
	path('cartapi/', views.CartApiView.as_view(), name='cart_api'),
	path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
	path('cart/add/<int:product_id>/', views.CartAddApiView.as_view(), name='cart_add_api'),
	path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
	path('cart/remove/<int:product_id>/', views.CartRemoveApiView.as_view(), name='cart_remove_api'),
	path('pay/<int:order_id>/', views.OrderPayView.as_view(), name='order_pay'),
	path('verify/', views.OrderVerifyView.as_view(), name='order_verify'),
	path('apply/<int:order_id>/', views.CouponApplyView.as_view(), name='apply_coupon'),
]
