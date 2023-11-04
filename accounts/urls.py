from django.urls import path
from .views import UserLogoutView,UserRegisterVerifyCodeView,UserLoginView,UserRegisterView,UserPasswordResetView,UserPasswordResetCompleteView,UserPasswordResetConfirmView,UserPasswordResetDoneView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'accounts'
urlpatterns = [
	path('register/', UserRegisterView.as_view(), name='user_register'),
	# path('registerapi/', UserRegisterApiView.as_view(), name='user_registerapi'),
	# path('loginapi/', UserLoginApiView.as_view(), name='user_loginapi'),
	path('verify/', UserRegisterVerifyCodeView.as_view(), name='verify_code'),
	path('login/', UserLoginView.as_view(), name='user_login'),
	path('logout/', UserLogoutView.as_view(), name='user_logout'),
	path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/register/', RegisterView.as_view(), name="sign_up"),
    path('reset/', UserPasswordResetView.as_view(), name='reset_password'),
	path('reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
	path('confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('confirm/complete', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]