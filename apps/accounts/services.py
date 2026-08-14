from .models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed


class RegisterUserService:
    @staticmethod
    def user_registration(validated_data):

        password = validated_data.pop("password")

        user = User(**validated_data)

        user.set_password(password)

        user.save()

        return user

    @staticmethod
    def user_login(validated_data):

        email = validated_data["email"]
        password = validated_data["password"]

        user = authenticate(
            email=email,
            password=password,
        )

        if user is None:
            raise AuthenticationFailed("Invalid email or password.")

        if not user.is_active:
            raise AuthenticationFailed("Your account is inactive.")

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "phone": user.phone,
                "role": user.role,
                "branch": user.branch.id if user.branch else None,
                "church": user.church.id if user.church else None,
            },
        }

    @staticmethod
    def get_all_register_user():
        user = User.objects.all()
        return user

    @staticmethod
    def numbers_of_users():
        users = User.objects.all()
        return users
