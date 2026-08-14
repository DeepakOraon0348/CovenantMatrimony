from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import FamilySerializer
from .services import FamilyService


class CreateFamilyAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, profile_id):

        serializer = FamilySerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        try:

            family = FamilyService.create_family(
                profile_id=profile_id,
                user=request.user,
                validated_data=serializer.validated_data,
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
                "message": "Family details created successfully.",
                "data": FamilySerializer(family).data,
            },
            status=status.HTTP_201_CREATED,
        )

class GetMyFamilyAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile_id = request.query_params.get("profile_id")

        family = FamilyService.get_my_family(
            profile_id=profile_id,
            user=request.user,
        )

        return Response(
            {
                "message": "Family details fetched successfully.",
                "data": FamilySerializer(family).data,
            },
            status=status.HTTP_200_OK,
        )


class UpdateFamilyAPI(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, profile_id):

        serializer = FamilySerializer(
            data=request.data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True
        )

        family = FamilyService.update_family(
            profile_id=profile_id,
            user=request.user,
            validated_data=serializer.validated_data,
        )

        return Response(
            {
                "message": "Family details updated successfully.",
                "data": FamilySerializer(family).data,
            },
            status=status.HTTP_200_OK,
        )


class DeleteFamilyAPI(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request):
        profile_id=request.query_params.get("profile_id")

        FamilyService.delete_family(
            profile_id=profile_id,
            user=request.user,
        )

        return Response(
            {
                "message": "Family details deleted successfully."
            },
            status=status.HTTP_200_OK,
        )