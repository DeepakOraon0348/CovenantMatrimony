from django.db import models

from apps.accounts.models import User
from apps.user_subscriptions.models import UserSubscription
from apps.subscriptions.models import SubscriptionPlan


class PaymentStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    SUCCESS = "SUCCESS", "Success"
    FAILED = "FAILED", "Failed"


class PaymentMethod(models.TextChoices):
    RAZORPAY = "RAZORPAY", "Razorpay"


class Payment(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="payments",
    )

    plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.PROTECT,
        related_name="payments",
    )

    user_subscription = models.ForeignKey(
        UserSubscription,
        on_delete=models.PROTECT,
        related_name="payments",
        null=True,
        blank=True,
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.RAZORPAY,
    )

    transaction_id = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )

    razorpay_order_id = models.CharField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
    )

    razorpay_payment_id = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    razorpay_signature = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
    )

    paid_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.user.email} - {self.amount}"