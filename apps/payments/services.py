import razorpay

from decimal import Decimal

from django.conf import settings
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone

from apps.accounts.models import User
from apps.profiles.models import Profile
from apps.subscriptions.models import SubscriptionPlan
from apps.user_subscriptions.models import UserSubscription

from .models import Payment, PaymentStatus


class PaymentService:

    @staticmethod
    def get_razorpay_client():

        return razorpay.Client(
            auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET,
            )
        )

    # ==========================================================
    # CREATE RAZORPAY ORDER
    # ==========================================================

    @staticmethod
    def create_payment(user, plan_id):
        print("KEY ID:", settings.RAZORPAY_KEY_ID)
        print(
         "SECRET AVAILABLE:",
        bool(settings.RAZORPAY_KEY_SECRET)
        )

        plan = get_object_or_404(
            SubscriptionPlan,
            id=plan_id,
            is_active=True,
        )

        if plan.price <= 0:

            raise ValueError(
                "Subscription plan price must be greater than zero."
            )

        # ------------------------------------------------------
        # Amount in rupees
        # ------------------------------------------------------

        amount = Decimal(plan.price)

        # Razorpay requires amount in paise.
        amount_in_paise = int(
            amount * Decimal("100")
        )

        # ------------------------------------------------------
        # Create Razorpay client
        # ------------------------------------------------------

        client = PaymentService.get_razorpay_client()

        # ------------------------------------------------------
        # Create Razorpay order
        # ------------------------------------------------------

        razorpay_order = client.order.create(
            {
                "amount": amount_in_paise,
                "currency": settings.RAZORPAY_CURRENCY,
                "receipt": f"payment_{user.id}_{plan.id}",
                "notes": {
                    "user_id": str(user.id),
                    "plan_id": str(plan.id),
                    "plan_name": plan.name,
                },
                "payment_capture": 1,
            }
        )

        # ------------------------------------------------------
        # Create local payment
        # ------------------------------------------------------

        payment = Payment.objects.create(
            user=user,
            plan=plan,
            amount=amount,
            razorpay_order_id=razorpay_order["id"],
            payment_status=PaymentStatus.PENDING,
        )

        return payment, razorpay_order
    
    
    # ==========================================================
    # VERIFY PAYMENT
    # ==========================================================

    @staticmethod
    @transaction.atomic
    def verify_payment(
        user,
        razorpay_payment_id,
        razorpay_order_id,
        razorpay_signature,
    ):

        payment = get_object_or_404(
            Payment,
            user=user,
            razorpay_order_id=razorpay_order_id,
        )

        # ------------------------------------------------------
        # Prevent duplicate verification
        # ------------------------------------------------------

        if payment.payment_status == PaymentStatus.SUCCESS:

            return payment

        # ------------------------------------------------------
        # Verify Razorpay signature
        # ------------------------------------------------------

        client = PaymentService.get_razorpay_client()

        try:

            client.utility.verify_payment_signature(
                {
                    "razorpay_order_id": razorpay_order_id,
                    "razorpay_payment_id": razorpay_payment_id,
                    "razorpay_signature": razorpay_signature,
                }
            )

        except razorpay.errors.SignatureVerificationError:

            payment.payment_status = PaymentStatus.FAILED

            payment.save(
                update_fields=[
                    "payment_status",
                    "updated_at",
                ]
            )

            raise ValueError(
                "Payment signature verification failed."
            )

        # ------------------------------------------------------
        # Store Razorpay payment information
        # ------------------------------------------------------

        payment.razorpay_payment_id = (
            razorpay_payment_id
        )

        payment.razorpay_signature = (
            razorpay_signature
        )

        payment.transaction_id = (
            razorpay_payment_id
        )

        payment.payment_status = (
            PaymentStatus.SUCCESS
        )

        payment.paid_at = timezone.now()

        payment.save()

        # ------------------------------------------------------
        # Create UserSubscription
        # ------------------------------------------------------

        start_date = timezone.now()

        expiry_date = (
            start_date
            + timezone.timedelta(
                days=payment.plan.duration_days
            )
        )

        user_subscription = UserSubscription.objects.create(
            user=user,
            plan=payment.plan,
            start_date=start_date,
            expiry_date=expiry_date,
            is_active=True,
        )

        # ------------------------------------------------------
        # Link payment with subscription
        # ------------------------------------------------------

        payment.user_subscription = (
            user_subscription
        )

        payment.save(
            update_fields=[
                "user_subscription",
                "updated_at",
            ]
        )

        # ------------------------------------------------------
        # Make profile photo visible
        # ------------------------------------------------------

        try:

            profile = user.profile

            profile.is_photo_visible = True

            profile.save(
                update_fields=[
                    "is_photo_visible",
                    "updated_at",
                ]
            )

        except Profile.DoesNotExist:

            pass

        return payment