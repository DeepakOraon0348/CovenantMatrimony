import re
from rest_framework import serializers
from .models import Church


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

    return value


def validate_pastor_name(value):
    value = value.strip()

    if len(value) < 3:
        raise serializers.ValidationError(
            "Pastor name must contain at least 3 characters."
        )

    if not re.fullmatch(r"(Rev\.|Pastor)\s+[A-Za-z]+(?:[ '-][A-Za-z]+)*", value):
        raise serializers.ValidationError(
            "Pastor name must start with 'Rev.' or 'Pastor', followed by a valid name."
        )

    return value


def validate_email(value):
    value = value.lower().strip()

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(pattern, value):
        raise serializers.ValidationError("Enter a valid email address.")

    if Church.objects.filter(email=value).exists():
        raise serializers.ValidationError("This email is already registered.")

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


def validate_church_code(value):
    value = value.upper().strip()

    if not re.fullmatch(r"^[A-Z]{2,5}[0-9]{2,5}$", value):
        raise serializers.ValidationError("Invalid church code.")

    if Church.objects.filter(code=value).exists():
        raise serializers.ValidationError("This church code is already registered.")

    return value


def update_validate_name(value):
    value = value.strip()

    if len(value) < 3:
        raise serializers.ValidationError(
            "Church name must contain at least 3 characters."
        )

    if not re.fullmatch(r"[A-Za-z0-9 .&'()-]+", value):
        raise serializers.ValidationError(
            "Church name can contain only letters, numbers, spaces, periods (.), apostrophes ('), hyphens (-), parentheses (), and ampersands (&)."
        )

    return value


def update_validate_pastor_name(value):
    value = value.strip()

    if len(value) < 3:
        raise serializers.ValidationError(
            "Pastor name must contain at least 3 characters."
        )

    if not re.fullmatch(r"(Rev\.|Pastor)\s+[A-Za-z]+(?:[ '-][A-Za-z]+)*", value):
        raise serializers.ValidationError(
            "Pastor name must start with 'Rev.' or 'Pastor', followed by a valid name."
        )

    return value


def update_validate_email(value):
    value = value.lower().strip()

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(pattern, value):
        raise serializers.ValidationError("Enter a valid email address.")

    return value


def update_validate_phone(value):
    value = value.strip()

    if not re.fullmatch(r"^[6-9]\d{9}$", value):
        raise serializers.ValidationError("Enter a valid 10-digit mobile number.")

    return value


def update_validate_pincode(value):
    value = value.strip()

    if not re.fullmatch(r"^\d{6}$", value):
        raise serializers.ValidationError("Pincode must contain 6 digits.")

    return value


def update_validate_church_code(value):
    value = value.upper().strip()

    if not re.fullmatch(r"^[A-Z]{2,5}[0-9]{2,5}$", value):
        raise serializers.ValidationError("Invalid church code.")

    return value
