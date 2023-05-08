from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = User
		fields = ('full_name','phone_number' , 'password', 'password2')
		extra_kwargs = {
			'password': {'write_only':True},
		}

	def create(self, validated_data):
		del validated_data['password2']
		return User.objects.create_user(**validated_data)


	# def validate_full_name(value):
	# 	if value == 'admin':
	# 		raise serializers.ValidationError('username cant be `admin`')
	# 	return value

	def validate(self, data):
		if data['password'] != data['password2']:
			raise serializers.ValidationError('passwords must match')
		return data


class UserSerializer(serializers.ModelSerializer):
	class Meta :
		model = User
		fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
	# password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = User
		fields = ('phone_number' , 'password',)
		extra_kwargs = {
			'password': {'write_only':True},
		}