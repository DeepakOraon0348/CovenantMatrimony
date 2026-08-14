import re

from rest_framework import serializers

from .models import User


def validate_first_name(value):
    value = value.strip()

    if len(value) < 2:
        raise serializers.ValidationError(
            "First name must contain at least 2 characters."
        )

    if not re.fullmatch(r"[A-Za-z]+(?: [A-Za-z]+)*", value):
        raise serializers.ValidationError(
            "First name should contain only letters and spaces."
        )

    return value.title()


def validate_last_name(value):
    value = value.strip()

    if len(value) < 2:
        raise serializers.ValidationError(
            "Last name must contain at least 2 characters."
        )

    if not re.fullmatch(r"[A-Za-z]+(?: [A-Za-z]+)*", value):
        raise serializers.ValidationError(
            "Last name should contain only letters and spaces."
        )

    return value.title()


def validate_email(value):
    value = value.lower().strip()

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.fullmatch(pattern, value):
        raise serializers.ValidationError("Enter a valid email address.")

    if User.objects.filter(email=value).exists():
        raise serializers.ValidationError("Email already exists.")

    return value


def validate_phone(value):
    value = value.strip()

    if not re.fullmatch(r"^[6-9]\d{9}$", value):
        raise serializers.ValidationError("Enter a valid 10-digit mobile number.")

    if User.objects.filter(phone=value).exists():
        raise serializers.ValidationError("Phone number already exists.")

    return value


def validate_password(value):

    if len(value) < 8:
        raise serializers.ValidationError(
            "Password must contain at least 8 characters."
        )

    if not re.search(r"[A-Z]", value):
        raise serializers.ValidationError(
            "Password must contain at least one uppercase letter."
        )

    if not re.search(r"[a-z]", value):
        raise serializers.ValidationError(
            "Password must contain at least one lowercase letter."
        )

    if not re.search(r"\d", value):
        raise serializers.ValidationError("Password must contain at least one number.")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
        raise serializers.ValidationError(
            "Password must contain at least one special character."
        )

    return value
