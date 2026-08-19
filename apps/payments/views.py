from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models import User
from apps.payments.models import Payment
from django.shortcuts import get_object_or_404

from .serializers import (
    PaymentSerializer,
    VerifyPaymentSerializer,
)

from .services import PaymentService


class CreatePaymentAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        plan_id = request.data.get("plan_id")
        user_id = request.data.get("user_id")
        if not plan_id:

            return Response(
                {
                    "message": "plan_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
            # --------------------------------------------------
        # Validate user_id
        # --------------------------------------------------

        if not user_id:
            return Response(
                {
                    "message": "user_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        # --------------------------------------------------
        # Get User object
        # --------------------------------------------------

        try:
            user = User.objects.get(id=user_id)

        except User.DoesNotExist:
            return Response(
                {
                    "message": "User not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )


        try:

            payment, razorpay_order = (
                PaymentService.create_payment(
                    user=user,
                    plan_id=plan_id,
                )
            )

        except ValueError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": "Razorpay order created successfully.",

                "data": {
                    "payment_id": payment.id,

                    "razorpay_key_id": (
                        settings.RAZORPAY_KEY_ID
                    ),

                    "razorpay_order_id": (
                        razorpay_order["id"]
                    ),

                    "amount": (
                        razorpay_order["amount"]
                    ),

                    "currency": (
                        razorpay_order["currency"]
                    ),

                    "plan": payment.plan.name,
                },
            },
            status=status.HTTP_201_CREATED,
        )
        
class VerifyPaymentAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = VerifyPaymentSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        try:

            payment = PaymentService.verify_payment(
                user=request.user,
                razorpay_payment_id=(
                    serializer.validated_data[
                        "razorpay_payment_id"
                    ]
                ),
                razorpay_order_id=(
                    serializer.validated_data[
                        "razorpay_order_id"
                    ]
                ),
                razorpay_signature=(
                    serializer.validated_data[
                        "razorpay_signature"
                    ]
                ),
            )

        except ValueError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": (
                    "Payment verified successfully."
                ),
                "data": PaymentSerializer(
                    payment
                ).data,
            },
            status=status.HTTP_200_OK,
        )

class GetMyPaymentsAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        payments = (
            request.user.payments
            .select_related(
                "plan",
                "user_subscription",
            )
            .order_by("-created_at")
        )

        return Response(
            {
                "message": (
                    "Payments fetched successfully."
                ),
                "data": PaymentSerializer(
                    payments,
                    many=True,
                ).data,
            },
            status=status.HTTP_200_OK,
        )
        
class GetPaymentAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        payment_id=request.query_params.get("payment_id")

        from django.shortcuts import get_object_or_404

        payment = get_object_or_404(
            Payment,
            id=payment_id,
            user=request.user,
        )

        return Response(
            {
                "message": (
                    "Payment fetched successfully."
                ),
                "data": PaymentSerializer(
                    payment
                ).data,
            },
            status=status.HTTP_200_OK,
        )
        
class AdminVerifyPaymentAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = VerifyPaymentSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        try:

            payment = PaymentService.verify_payment_by_admin(
                razorpay_payment_id=(
                    serializer.validated_data[
                        "razorpay_payment_id"
                    ]
                ),
                razorpay_order_id=(
                    serializer.validated_data[
                        "razorpay_order_id"
                    ]
                ),
                razorpay_signature=(
                    serializer.validated_data[
                        "razorpay_signature"
                    ]
                ),
            )

        except ValueError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": "Payment verified successfully.",
                "data": PaymentSerializer(payment).data,
            },
            status=status.HTTP_200_OK,
        )