
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import SubscriptionPlan
from .serializers import *
from .services import SubscriptionPlanService


class CreateSubscriptionPlanAPI(APIView):

    def post(self, request):

        serializer = CreateSubscriptionPlanSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        plan = SubscriptionPlanService.create_subscription_plan(
            serializer.validated_data
        )

        response_serializer = SubscriptionPlanSerializer(plan)

        return Response(
            {
                "success": True,
                "message": "Subscription plan created successfully.",
                "data": response_serializer.data,
            },
            status=status.HTTP_201_CREATED
        )


class GetAllSubscriptionPlansAPI(APIView):

    def get(self, request):

        plans = SubscriptionPlanService.get_all_subscription_plans()

        serializer = SubscriptionPlanSerializer(
            plans,
            many=True
        )

        return Response(
            {
                "success": True,
                "message": "Subscription plans fetched successfully.",
                "total":len(serializer.data),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
        )


class GetSubscriptionPlanAPI(APIView):

    def get(self, request):
        plane_id=request.query_params.get("plane_id")
        
        if not plane_id:
            return Response(
                {
                    "message":"Plan id required.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            plan = SubscriptionPlanService.get_subscription_plan(plane_id=plane_id)

        except SubscriptionPlan.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Subscription plan not found.",
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SubscriptionPlanSerializer(plan)

        return Response(
            {
                "success": True,
                "message": "Subscription plan fetched successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
        )


class UpdateSubscriptionPlanAPI(APIView):

    def put(self, request, plane_id):

        try:
            plan = SubscriptionPlanService.get_subscription_plan(plane_id)

        except SubscriptionPlan.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Subscription plan not found.",
                },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UpdateSubscriptionPlanSerializer(
            plan,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        updated_plan = SubscriptionPlanService.update_subscription_plan(
            plane_id,
            serializer.validated_data
        )

        response_serializer = SubscriptionPlanSerializer(
            updated_plan
        )

        return Response(
            {
                "success": True,
                "message": "Subscription plan updated successfully.",
                "data": response_serializer.data,
            },
            status=status.HTTP_200_OK
        )


class DeleteSubscriptionPlanAPI(APIView):

    def delete(self, request):
        plane_id=request.query_params.get("plane_id")

        try:
            plan = SubscriptionPlanService.get_subscription_plan(plane_id=plane_id)

        except SubscriptionPlan.DoesNotExist:

            return Response(
                {
                    "success": False,
                    "message": "Subscription plan not found.",
                },
                status=status.HTTP_404_NOT_FOUND
            )

        SubscriptionPlanService.delete_subscription_plan(plane_id)

        return Response(
            {
                "success": True,
                "message": "Subscription plan deleted successfully.",
            },
            status=status.HTTP_200_OK
        )

