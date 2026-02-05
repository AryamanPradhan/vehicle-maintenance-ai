from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if not username or not password:
            raise serializers.ValidationError(
                "User and password required"
            )

        user = authenticate(username=username, password = password)

        if not user:
            raise serializers.ValidationError(
                "Invalid Credemntials"
            )
    
        if not user.is_active:
            raise serializers.ValidationError(
                "User account is Disabled"
            )
        attrs["users"] = user
        return attrs


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=140)
    middle_name = serializers.CharField(
        max_length=150, required=False, allow_blank=True
    )
    last_name = serializers.CharField(max_length=150)
    phone = serializers.CharField(max_length=10)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def create(self, validated_data):
        middle_name = validated_data.pop("middle_name", "")
        password = validated_data.pop("password")

        user = User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            password=password,
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        UserProfile.objects.create(
            user=user,
            middle_name=middle_name,
            phone=validated_data["phone"],
        )

        return user