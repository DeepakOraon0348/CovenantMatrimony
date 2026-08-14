from rest_framework import serializers

from apps.subscriptions.models import SubscriptionPlan


def validate_subscription_plan(plan_id):

    try:
        plan = SubscriptionPlan.objects.get(
            id=plan_id,
            is_active=True,
        )
    except SubscriptionPlan.DoesNotExist:
        raise serializers.ValidationError(
            "Subscription plan does not exist or is inactive."
        )

    if plan.price <= 0:
        raise serializers.ValidationError(
            "Subscription plan price must be greater than zero."
        )

    if plan.duration_days <= 0:
        raise serializers.ValidationError(
            "Subscription plan duration must be greater than zero."
        )

    return plan