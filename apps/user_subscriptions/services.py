from datetime import timedelta

from django.shortcuts import get_object_or_404
from django.utils import timezone

from apps.subscriptions.models import SubscriptionPlan

from .models import UserSubscription


class UserSubscriptionService:

    @staticmethod
    def create_subscription(
        user,
        plan_id,
    ):

        plan = get_object_or_404(
            SubscriptionPlan,
            id=plan_id,
        )

        now = timezone.now()

        # Check whether user already has active subscription
        active_subscription = (
            UserSubscription.objects.filter(
                user=user,
                is_active=True,
                expiry_date__gt=now,
            )
            .first()
        )

        if active_subscription:

            raise ValueError(
                "User already has an active subscription."
            )

        # Calculate expiry date
        expiry_date = (
            now
            + timedelta(
                days=plan.duration_days
            )
        )

        subscription = UserSubscription.objects.create(
            user=user,
            plan=plan,
            start_date=now,
            expiry_date=expiry_date,
            is_active=True,
        )

        return subscription
    
    @staticmethod
    def get_my_subscription(user):

        subscription = (
            UserSubscription.objects
            .filter(
                user=user,
                is_active=True,
            )
            .order_by("-created_at")
            .first()
        )

        if not subscription:

            raise ValueError(
                "No active subscription found."
            )

        return subscription
    
    @staticmethod
    def get_subscription_by_id(subscription_id, user):

        subscription = get_object_or_404(
            UserSubscription,
            id=subscription_id,
            user=user,
        )

        return subscription
    
    @staticmethod
    def cancel_subscription(
        subscription_id,
        user,
    ):

        subscription = get_object_or_404(
            UserSubscription,
            id=subscription_id,
            user=user,
       )

        if not subscription.is_active:

            raise ValueError(
                "Subscription is already inactive."
            )

        subscription.is_active = False

        subscription.save(
            update_fields=[
                "is_active",
                "updated_at",
            ]
        )

        # Hide profile photo
        if hasattr(user, "profile"):

            profile = user.profile

            profile.is_photo_visible = False

        profile.save(
            update_fields=[
                "is_photo_visible",
                "updated_at",
            ]
        )

        return subscription
    
    @staticmethod
    def expire_subscriptions():

        now = timezone.now()

        expired_subscriptions = (
            UserSubscription.objects.filter(
                is_active=True,
                expiry_date__lte=now,
            )
        )

        expired_count = 0

        for subscription in expired_subscriptions:

            subscription.is_active = False

            subscription.save(
                update_fields=[
                    "is_active",
                    "updated_at",
                ]
            )

        user = subscription.user

        if hasattr(user, "profile"):

            profile = user.profile

            # Check if user has another active subscription
            another_active_subscription = (
                UserSubscription.objects.filter(
                    user=user,
                    is_active=True,
                    expiry_date__gt=now,
                )
                .exclude(
                    id=subscription.id
                )
                .exists()
            )

            if not another_active_subscription:

                profile.is_photo_visible = False

                profile.save(
                    update_fields=[
                        "is_photo_visible",
                        "updated_at",
                    ]
                )

        expired_count += 1

        return expired_count