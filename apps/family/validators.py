import re

from rest_framework import serializers


def validate_name(value):

    value = value.strip()

    if len(value) < 2:
        raise serializers.ValidationError(
            "Name must contain at least 2 characters."
        )

    if not re.fullmatch(
        r"[A-Za-z]+(?: [A-Za-z]+)*",
        value,
    ):
        raise serializers.ValidationError(
            "Name should contain only letters and spaces."
        )

    return value.title()


def validate_occupation(value):

    value = value.strip()

    if not value:
        return value

    if len(value) < 2:
        raise serializers.ValidationError(
            "Occupation must contain at least 2 characters."
        )

    return value


def validate_siblings(value):

    if value < 0:
        raise serializers.ValidationError(
            "Number of brothers or sisters cannot be negative."
        )

    return value