from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.meetings.models import Meeting

from .models import Marriage

from .serializers import (
    MarriageSerializer,
    CreateMarriageSerializer,
    UpdateMarriageSerializer,
    UpdateMarriageStatusSerializer,
)

from .services import MarriageService


# ==========================================================
# CREATE MARRIAGE
# ==========================================================

class CreateMarriageAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        serializer = CreateMarriageSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        meeting = serializer.validated_data[
            "meeting"
        ]

        marriage_date = (
            serializer.validated_data[
                "marriage_date"
            ]
        )

        venue = serializer.validated_data[
            "venue"
        ]

        pastor_name = (
            serializer.validated_data[
                "pastor_name"
            ]
        )

        remarks = serializer.validated_data.get(
            "remarks"
        )

        try:

            marriage = (
                MarriageService.create_marriage(
                    user=request.user,
                    meeting=meeting,
                    marriage_date=marriage_date,
                    venue=venue,
                    pastor_name=pastor_name,
                    remarks=remarks,
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
                    "Marriage created successfully."
                ),
                "data": MarriageSerializer(
                    marriage
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )


# ==========================================================
# GET ALL MARRIAGES
# ==========================================================

class GetAllMarriageAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        try:

            marriages = (
                MarriageService
                .get_all_marriages()
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = MarriageSerializer(
            marriages,
            many=True,
        )

        return Response(
            {
                "message": (
                    "All marriages retrieved successfully."
                ),
                "total": marriages.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# ==========================================================
# GET MY MARRIAGES
# ==========================================================

class GetMyMarriageAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        marriages = (
            MarriageService
            .get_my_marriages(
                user=request.user
            )
        )

        serializer = MarriageSerializer(
            marriages,
            many=True,
        )

        return Response(
            {
                "message": (
                    "My marriages retrieved successfully."
                ),
                "total": marriages.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# ==========================================================
# GET MARRIAGE BY ID
# ==========================================================

class GetMarriageAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):
        marriage_id=request.query_params.get("marriage_id")
        print("marriage id is :", marriage_id)
        if not marriage_id:
            return Response(
                {
                    "message":"Marriage id required.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            marriage = (
                MarriageService
                .get_marriage_by_id(
                    marriage_id
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

            MarriageService.validate_marriage_access(
                user=request.user,
                marriage=marriage,
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
                    "Marriage retrieved successfully."
                ),
                "data": MarriageSerializer(
                    marriage
                ).data,
            },
            status=status.HTTP_200_OK,
        )


# ==========================================================
# UPDATE MARRIAGE
# ==========================================================

class UpdateMarriageAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def put(
        self,
        request,
        marriage_id,
    ):

        try:

            marriage = (
                MarriageService
                .get_marriage_by_id(
                    marriage_id
                )
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = UpdateMarriageSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        try:

            marriage = (
                MarriageService
                .update_marriage(
                    user=request.user,
                    marriage=marriage,
                    marriage_date=(
                        serializer.validated_data[
                            "marriage_date"
                        ]
                    ),
                    venue=(
                        serializer.validated_data[
                            "venue"
                        ]
                    ),
                    pastor_name=(
                        serializer.validated_data[
                            "pastor_name"
                        ]
                    ),
                    remarks=(
                        serializer.validated_data.get(
                            "remarks"
                        )
                    ),
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
                    "Marriage updated successfully."
                ),
                "data": MarriageSerializer(
                    marriage
                ).data,
            },
            status=status.HTTP_200_OK,
        )


# ==========================================================
# UPDATE STATUS
# ==========================================================

class UpdateMarriageStatusAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def patch(self, request):
        marriage_id=request.query_params.get("marriage_id")
        if not marriage_id:
            return Response(
                {
                    "message":"marriage id required.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            marriage = (
                MarriageService
                .get_marriage_by_id(
                    marriage_id
                )
            )

        except ValidationError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = (
            UpdateMarriageStatusSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        try:

            marriage = (
                MarriageService
                .update_status(
                    user=request.user,
                    marriage=marriage,
                    status=(
                        serializer.validated_data[
                            "status"
                        ]
                    ),
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
                    "Marriage status updated successfully."
                ),
                "data": MarriageSerializer(
                    marriage
                ).data,
            },
            status=status.HTTP_200_OK,
        )


# ==========================================================
# DELETE MARRIAGE
# ==========================================================

class DeleteMarriageAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def delete(
        self,
        request,
        marriage_id,
    ):

        try:

            marriage = (
                MarriageService
                .get_marriage_by_id(
                    marriage_id
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

            MarriageService.delete_marriage(
                user=request.user,
                marriage=marriage,
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
                    "Marriage deleted successfully."
                )
            },
            status=status.HTTP_200_OK,
        )