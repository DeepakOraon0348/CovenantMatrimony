
from rest_framework import serializers

from .models import SubscriptionPlan
from .validators import (
    validate_name,
    validate_price,
    validate_duration_days,
    validate_max_matches_per_day,
)


class SubscriptionPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionPlan
        fields = [
            "id",
            "name",
            "price",
            "duration_days",
            "max_matches_per_day",
            "featured_profiles",
            "priority_support",
            "is_active",
            "created_at",
            "updated_at",
        ]


class CreateSubscriptionPlanSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        validators=[validate_name]
    )

    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validate_price]
    )

    duration_days = serializers.IntegerField(
        validators=[validate_duration_days]
    )

    max_matches_per_day = serializers.IntegerField(
        default=0,
        validators=[validate_max_matches_per_day]
    )

    class Meta:
        model = SubscriptionPlan
        fields = [
            "name",
            "price",
            "duration_days",
            "max_matches_per_day",
            "featured_profiles",
            "priority_support",
            "is_active",
        ]

    def validate_name(self, value):
        if SubscriptionPlan.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                "A subscription plan with this name already exists."
            )

        return value


class UpdateSubscriptionPlanSerializer(serializers.ModelSerializer):

    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        validators=[validate_price]
    )

    duration_days = serializers.IntegerField(
        required=False,
        validators=[validate_duration_days]
    )

    max_matches_per_day = serializers.IntegerField(
        required=False,
        validators=[validate_max_matches_per_day]
    )

    class Meta:
        model = SubscriptionPlan
        fields = [
            "name",
            "price",
            "duration_days",
            "max_matches_per_day",
            "featured_profiles",
            "priority_support",
            "is_active",
        ]

    def validate_name(self, value):
        plan = self.instance

        if SubscriptionPlan.objects.filter(
            name=value
        ).exclude(id=plan.id).exists():

            raise serializers.ValidationError(
                "A subscription plan with this name already exists."
            )

        return value

