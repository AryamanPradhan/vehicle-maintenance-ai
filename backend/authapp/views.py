from urllib import request
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
import json
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer, RegisterSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user":{
                "id": user.id,
                "username": user.id,
                "email": user.email,
            },
        },
            status= status.HTTP_200_OK
        )



class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
        
        user = serializer.save()

        return Response({
            "message": "Registration Successful",
            "user_id": user.id,
            "email": user.email
        },
        status=status.HTTP_201_CREATED
        )