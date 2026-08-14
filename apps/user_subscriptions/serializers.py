from rest_framework import serializers

from apps.subscriptions.models import SubscriptionPlan

from .models import UserSubscription
from .validators import validate_plan


class UserSubscriptionSerializer(serializers.ModelSerializer):

    plan = serializers.PrimaryKeyRelatedField(
        queryset=SubscriptionPlan.objects.all(),
        validators=[validate_plan],
    )

    class Meta:

        model = UserSubscription

        fields = "__all__"

        read_only_fields = (
            "id",
            "user",
            "start_date",
            "expiry_date",
            "is_active",
            "created_at",
            "updated_at",
        )