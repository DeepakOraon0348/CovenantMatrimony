import code

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .serializers import *
from .services import *


# Create your views here.
class CreateAccountAPI(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User_registration = RegisterUserService.user_registration(
            serializer.validated_data
        )

        return Response(
            {
                "message": "User Register Sucessful.",
                "data": RegisterUserSerializer(User_registration).data,
            },
            status=status.HTTP_201_CREATED,
        )


class UserLoginAPI(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        login_response = RegisterUserService.user_login(serializer.validated_data)

        return Response(
            {
                "message": "Login Successful.",
                "data": login_response,
            },
            status=status.HTTP_200_OK,
        )


class GetAllRegisterUser(APIView):
    def get(self, request):
        user = RegisterUserService.get_all_register_user()
        serializer = RegisterUserSerializer(user, many=True)
        return Response(
            {"message": "Get All Register User.", "data": serializer.data},
            status=status.HTTP_200_OK,
        )


class NumbersOfRegisterUserAPI(APIView):
    def get(self, request):
        numbersOfuser = RegisterUserService.numbers_of_users()
        serializer = RegisterUserSerializer(numbersOfuser, many=True)
        return Response(
            {
                "message": "Total Numbers of Register Users.",
                "total": len(serializer.data),
            },
            status=status.HTTP_200_OK,
        )
