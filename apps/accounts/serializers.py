from rest_framework import serializers
from .models import *

from .validators import *


class RegisterUserSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(validators=[validate_first_name])

    last_name = serializers.CharField(validators=[validate_last_name])

    email = serializers.EmailField(validators=[validate_email])

    phone = serializers.CharField(validators=[validate_phone])

    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = "__all__"


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(write_only=True)
