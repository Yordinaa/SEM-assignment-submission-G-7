from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser  # Assuming CustomUser is the user model
from django.contrib.auth.password_validation import validate_password

# Serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'role')

    def create(self, validated_data):
        # Create a user with the provided data
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'USER'),
        )
        return user

# Serializer for user profile details
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  # Use CustomUser model (or another user model if you have one)
        fields = ('id', 'username', 'email', 'role', 'date_joined')  # Add any fields you'd like to show


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data.get('role', 'USER'),
        )
        return user
