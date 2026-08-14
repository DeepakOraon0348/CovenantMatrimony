from rest_framework import serializers

from apps.subscriptions.models import SubscriptionPlan


def validate_plan(value):

    if not SubscriptionPlan.objects.filter(
        id=value.id
    ).exists():

        raise serializers.ValidationError(
            "Selected subscription plan does not exist."
        )

    return value