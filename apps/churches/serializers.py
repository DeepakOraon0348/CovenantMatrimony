from rest_framework import serializers
from .models import *

from .validators import *


class CreateChurchSerializer(serializers.ModelSerializer):

    name = serializers.CharField(validators=[validate_name])
    pastor_name = serializers.CharField(validators=[validate_pastor_name])

    email = serializers.EmailField(validators=[validate_email])

    phone = serializers.CharField(validators=[validate_phone])

    pincode = serializers.CharField(validators=[validate_pincode])

    code = serializers.CharField(validators=[validate_church_code])

    class Meta:
        model = Church
        fields = "__all__"


class UpdateChurchSerializer(serializers.ModelSerializer):

    name = serializers.CharField(validators=[update_validate_name])
    pastor_name = serializers.CharField(validators=[update_validate_pastor_name])
    email = serializers.EmailField(validators=[update_validate_email])

    phone = serializers.CharField(validators=[update_validate_phone])

    pincode = serializers.CharField(validators=[update_validate_pincode])

    code = serializers.CharField(validators=[update_validate_church_code])

    class Meta:
        model = Church
        fields = "__all__"
