from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate, login
from .models import AppAdmin


class AdminActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AppAdmin
        fields = ['id', 'app_icon', 'app_name', 'app_link', 'app_category', 'sub_category', 'points']


# Serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


# Serializer for login authentication (optional, if needed for API use)
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()