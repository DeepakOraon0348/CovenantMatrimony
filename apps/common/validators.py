import re
from rest_framework import serializers
from .models import Denomination


def validate_name(value):
    value = value.strip()

    if len(value) < 3:
        raise serializers.ValidationError(
            "Church name must contain at least 3 characters."
        )

    if not re.fullmatch(r"[A-Za-z0-9 .&'()-]+", value):
        raise serializers.ValidationError(
            "Church name can contain only letters, numbers, spaces, periods (.), apostrophes ('), hyphens (-), parentheses (), and ampersands (&)."
        )
    if Denomination.objects.filter(name=value).exists():
        raise serializers.ValidationError("denomination already Exist")

    return value
