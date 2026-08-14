from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment

        fields = "__all__"

        read_only_fields = (
            "id",
            "user",
            "plan",
            "user_subscription",
            "amount",
            "payment_method",
            "transaction_id",
            "razorpay_order_id",
            "razorpay_payment_id",
            "razorpay_signature",
            "payment_status",
            "paid_at",
            "created_at",
            "updated_at",
        )


class CreatePaymentSerializer(serializers.Serializer):

    plan_id = serializers.IntegerField(
        min_value=1
    )


class VerifyPaymentSerializer(serializers.Serializer):

    razorpay_payment_id = serializers.CharField(
        max_length=255
    )

    razorpay_order_id = serializers.CharField(
        max_length=255
    )

    razorpay_signature = serializers.CharField(
        max_length=500
    )