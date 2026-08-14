from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.core.exceptions import ValidationError

from .models import Prayer

from .serializers import (
    PrayerSerializer,
    CreatePrayerSerializer,
    UpdatePrayerSerializer,
    UpdatePrayerStatusSerializer,
)

from .services import PrayerService


# ==========================================================
# CREATE PRAYER
# ==========================================================

class CreatePrayerAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = CreatePrayerSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        title = serializer.validated_data[
            "title"
        ]

        note = serializer.validated_data.get(
            "note"
        )

        try:

            prayer = PrayerService.create_prayer(
                user=request.user,
                title=title,
                note=note,
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": (
                    "Prayer created successfully."
                ),
                "data": PrayerSerializer(
                    prayer
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )


# ==========================================================
# GET ALL PRAYERS
# ==========================================================

class GetAllPrayerAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        try:

            prayers = (
                PrayerService
                .get_all_prayers()
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": (
                    "All prayers retrieved successfully."
                ),
                "total": prayers.count(),
                "data": PrayerSerializer(
                    prayers,
                    many=True,
                ).data,
            },
            status=status.HTTP_200_OK,
        )


# ==========================================================
# GET MY CHURCH PRAYERS
# ==========================================================

class GetMyChurchPrayerAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        try:

            prayers = (
                PrayerService
                .get_my_church_prayers(
                    user=request.user
                )
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": (
                    "Church prayers retrieved successfully."
                ),
                "total": prayers.count(),
                "data": PrayerSerializer(
                    prayers,
                    many=True,
                ).data,
            },
            status=status.HTTP_200_OK,
        )


# ==========================================================
# GET SINGLE PRAYER
# ==========================================================

class GetPrayerAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        prayer_id = (
            request.query_params.get(
                "prayer_id"
            )
        )

        if not prayer_id:

            return Response(
                {
                    "message": (
                        "prayer_id is required."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            prayer = (
                PrayerService
                .get_prayer_by_id(
                    prayer_id
                )
            )

            PrayerService.validate_prayer_access(
                user=request.user,
                prayer=prayer,
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "message": (
                    "Prayer retrieved successfully."
                ),
                "data": PrayerSerializer(
                    prayer
                ).data,
            },
            status=status.HTTP_200_OK,
        )


# ==========================================================
# UPDATE PRAYER
# ==========================================================

class UpdatePrayerAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(self, request):

        prayer_id = (
            request.query_params.get(
                "prayer_id"
            )
        )

        if not prayer_id:

            return Response(
                {
                    "message": (
                        "prayer_id is required."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            prayer = (
                PrayerService
                .get_prayer_by_id(
                    prayer_id
                )
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = UpdatePrayerSerializer(
            data=request.data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True
        )

        try:

            prayer = PrayerService.update_prayer(
                user=request.user,
                prayer=prayer,
                title=serializer.validated_data.get(
                    "title"
                ),
                note=serializer.validated_data.get(
                    "note"
                ),
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": (
                    "Prayer updated successfully."
                ),
                "data": PrayerSerializer(
                    prayer
                ).data,
            },
            status=status.HTTP_200_OK,
        )


# ==========================================================
# UPDATE PRAYER STATUS
# ==========================================================

class UpdatePrayerStatusAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(self, request):

        prayer_id = (
            request.query_params.get(
                "prayer_id"
            )
        )

        if not prayer_id:

            return Response(
                {
                    "message": (
                        "prayer_id is required."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UpdatePrayerStatusSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        try:

            prayer = (
                PrayerService
                .get_prayer_by_id(
                    prayer_id
                )
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:

            prayer = (
                PrayerService.update_status(
                    user=request.user,
                    prayer=prayer,
                    status=serializer.validated_data[
                        "status"
                    ],
                )
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": (
                    "Prayer status updated successfully."
                ),
                "data": PrayerSerializer(
                    prayer
                ).data,
            },
            status=status.HTTP_200_OK,
        )


# ==========================================================
# DELETE PRAYER
# ==========================================================

class DeletePrayerAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(self, request):

        prayer_id = (
            request.query_params.get(
                "prayer_id"
            )
        )

        if not prayer_id:

            return Response(
                {
                    "message": (
                        "prayer_id is required."
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            prayer = (
                PrayerService
                .get_prayer_by_id(
                    prayer_id
                )
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:

            PrayerService.delete_prayer(
                user=request.user,
                prayer=prayer,
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        return Response(
            {
                "message": (
                    "Prayer deleted successfully."
                )
            },
            status=status.HTTP_200_OK,
        )