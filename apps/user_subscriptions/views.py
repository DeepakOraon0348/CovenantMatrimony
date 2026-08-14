from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSubscriptionSerializer
from .services import UserSubscriptionService


class CreateUserSubscriptionAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = UserSubscriptionSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        plan = serializer.validated_data["plan"]

        try:

            subscription = (
                UserSubscriptionService
                .create_subscription(
                    user=request.user,
                    plan_id=plan.id,
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
                "message": (
                    "Subscription created successfully."
                ),
                "data": UserSubscriptionSerializer(
                    subscription
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )

class GetMySubscriptionAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):
        try:

            subscription = (
                UserSubscriptionService
                .get_my_subscription(
                    user=request.user
                )
            )

        except ValueError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "message": (
                    "Subscription fetched successfully."
                ),
                "data": UserSubscriptionSerializer(
                    subscription
                ).data,
            },
            status=status.HTTP_200_OK,
        )
class GetUserSubscriptionByIdAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]
    
    def get(self, request):
        subscription_id=request.query_params.get("subscription_id")
        
        if not subscription_id:
            return Response(
                {
                    "message":"Do not have active subscrition.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        subscription = (
            UserSubscriptionService
            .get_subscription_by_id(
                subscription_id=subscription_id,
                user=request.user,
            )
        )

        return Response(
            {
                "message": (
                    "Subscription fetched successfully."
                ),
                "data": UserSubscriptionSerializer(
                    subscription
                ).data,
            },
            status=status.HTTP_200_OK,
        )
class CancelUserSubscriptionAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(
        self,
        request
    ):
        
        subscription_id=request.query_params.get("subscription_id")
        try:

            subscription = (
                UserSubscriptionService
                .cancel_subscription(
                    subscription_id=subscription_id,
                    user=request.user,
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
                "message": (
                    "Subscription cancelled successfully."
                ),
                "data": UserSubscriptionSerializer(
                    subscription
                ).data,
            },
            status=status.HTTP_200_OK,
        )