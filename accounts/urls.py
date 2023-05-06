from django.urls import path
from .views import UserLogoutView,UserRegisterView,UserRegisterApiView,UserLoginView,UserRegisterVerifyCodeView,UserLoginApiView


app_name = 'accounts'
urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='user_register'),
	path('registerapi/', UserRegisterApiView.as_view(), name='user_registerapi'),
	path('loginapi/', UserLoginApiView.as_view(), name='user_loginapi'),
	path('verify/', UserRegisterVerifyCodeView.as_view(), name='verify_code'),
	path('login/', UserLoginView.as_view(), name='user_login'),
	path('logout/', UserLogoutView.as_view(), name='user_logout'),
]