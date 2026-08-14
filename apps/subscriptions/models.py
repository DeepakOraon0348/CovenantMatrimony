from django.db import models


class SubscriptionPlan(models.Model):

    class PlanName(models.TextChoices):
        FREE = "FREE", "Free"
        SILVER = "SILVER", "Silver"
        GOLD = "GOLD", "Gold"
        DIAMOND = "DIAMOND", "Diamond"

    name = models.CharField(
        max_length=20,
        choices=PlanName.choices,
        unique=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
    )

    duration_days = models.PositiveIntegerField()

    max_matches_per_day = models.PositiveIntegerField(
        default=0
    )

    featured_profiles = models.BooleanField(
        default=False
    )

    priority_support = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name