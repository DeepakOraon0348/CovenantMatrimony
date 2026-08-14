import re
from rest_framework import serializers
from .models import Branch


def validate_name(value):
    value = value.strip()

    if len(value) < 3:
        raise serializers.ValidationError("Name must contain at least 3 characters.")

    if not re.fullmatch(r"[A-Za-z ]+", value):
        raise serializers.ValidationError(
            "Name should contain only letters and spaces."
        )

    if not value:
        raise serializers.ValidationError("Branch name is required.")

    if len(value) < 2:
        raise serializers.ValidationError(
            "Branch name must be at least 2 characters long."
        )

    if Branch.objects.filter(name__iexact=value).exists():
        raise serializers.ValidationError("A branch with this name already exists.")

    return value


def validate_email(value):
    value = value.lower().strip()

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(pattern, value):
        raise serializers.ValidationError("Enter a valid email address.")

    return value


def validate_phone(value):
    value = value.strip()

    if not re.fullmatch(r"^[6-9]\d{9}$", value):
        raise serializers.ValidationError("Enter a valid 10-digit mobile number.")

    return value


def validate_pincode(value):
    value = value.strip()

    if not re.fullmatch(r"^\d{6}$", value):
        raise serializers.ValidationError("Pincode must contain 6 digits.")

    return value


def validate_branch_code(value):
    value = value.upper().strip()

    if not re.fullmatch(r"^[A-Z]{2,5}[0-9]{2,5}$", value):
        raise serializers.ValidationError("Invalid branch code.")

    return value
