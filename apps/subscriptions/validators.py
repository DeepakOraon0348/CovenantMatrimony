
from rest_framework import serializers


def validate_name(value):
    if not value:
        raise serializers.ValidationError(
            "Subscription plan name is required."
        )

    return value


def validate_price(value):
    if value < 0:
        raise serializers.ValidationError(
            "Price cannot be negative."
        )

    return value


def validate_duration_days(value):
    if value <= 0:
        raise serializers.ValidationError(
            "Duration must be greater than 0 days."
        )

    return value


def validate_max_matches_per_day(value):
    if value < 0:
        raise serializers.ValidationError(
            "Maximum matches per day cannot be negative."
        )

    return value
