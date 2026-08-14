from rest_framework import serializers
from .models import *

from .validators import *


class CreateBranchSerializer(serializers.ModelSerializer):

    name = serializers.CharField(validators=[validate_name])

    email = serializers.EmailField(validators=[validate_email])

    phone = serializers.CharField(validators=[validate_phone])

    pincode = serializers.CharField(validators=[validate_pincode])

    code = serializers.CharField(validators=[validate_branch_code])

    class Meta:
        model = Branch
        fields = "__all__"
