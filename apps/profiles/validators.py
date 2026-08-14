import re

from rest_framework import serializers

from .models import Profile


def validate_profile_id(value):
    value = value.strip().upper()

    if len(value) < 5:
        raise serializers.ValidationError(
            "Profile ID must contain at least 5 characters."
        )

    if Profile.objects.filter(profile_id=value).exists():
        raise serializers.ValidationError("Profile ID already exists.")

    return value


def validate_height(value):
    if value <= 0:
        raise serializers.ValidationError("Height must be greater than 0.")

    if value < 3 or value > 8:
        raise serializers.ValidationError("Height must be between 3 and 8 feet.")

    return value


def validate_weight(value):
    if value <= 0:
        raise serializers.ValidationError("Weight must be greater than 0.")

    if value < 20 or value > 250:
        raise serializers.ValidationError("Enter a valid weight.")

    return value


def validate_education(value):
    value = value.strip()

    if len(value) < 2:
        raise serializers.ValidationError(
            "Education must contain at least 2 characters."
        )

    return value.title()


def validate_occupation(value):
    value = value.strip()

    if len(value) < 2:
        raise serializers.ValidationError(
            "Occupation must contain at least 2 characters."
        )

    return value.title()


def validate_annual_income(value):
    if value is not None and value < 0:
        raise serializers.ValidationError("Annual income cannot be negative.")

    return value


def validate_about_me(value):
    value = value.strip()

    if len(value) < 20:
        raise serializers.ValidationError(
            "About Me must contain at least 20 characters."
        )

    return value


def validate_height(value):
    if value < 3 or value > 8:
        raise serializers.ValidationError("Height must be between 3 and 8 feet.")
    return value


def validate_weight(value):
    if value <= 0:
        raise serializers.ValidationError("Weight must be greater than zero.")
    return value


def validate_education(value):
    if len(value.strip()) < 2:
        raise serializers.ValidationError("Education is required.")
    return value


def validate_occupation(value):
    if len(value.strip()) < 2:
        raise serializers.ValidationError("Occupation is required.")
    return value


def validate_annual_income(value):
    if value is not None and value < 0:
        raise serializers.ValidationError("Annual income cannot be negative.")
    return value


def validate_about_me(value):
    if len(value.strip()) < 20:
        raise serializers.ValidationError(
            "About Me should contain at least 20 characters."
        )
    return value


def validate_age(value):
    try:
        value = int(value)
    except (TypeError, ValueError):
        raise serializers.ValidationError("Age must be a number.")

    if value < 18 or value > 100:
        raise serializers.ValidationError("Age must be between 18 and 100.")

    return value
