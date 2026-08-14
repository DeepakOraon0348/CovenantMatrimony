import code
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .services import *


# Create your views here.
class CreateProfileAPI(APIView):
    def post(self, request):
        serializer = ProfileSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        created_church = ProfileService.create_Profile(serializer.validated_data)
        return Response(
            {
                "message": "Profile created successfully.",
                "data": ProfileSerializers(created_church).data,
            },
            status=status.HTTP_201_CREATED,
        )


class UpdateProfileAPI(APIView):

    def put(self, request, profile_id):

        serializer = UpdateProfileSerializer(
            data=request.data,
            partial=True,
        )

        serializer.is_valid(raise_exception=True)

        profile = ProfileService.update_profile(
            profile_id,
            serializer.validated_data,
        )

        return Response(
            {
                "message": "Profile updated successfully.",
                "data": UpdateProfileSerializer(profile).data,
            },
            status=status.HTTP_200_OK,
        )


class DeleteProfileAPI(APIView):

    def delete(self, request):
        profile_id = request.query_params.get("profile_id")

        deleteProfile = ProfileService.delete_profile(profile_id=profile_id)

        return Response(
            {
                "message": "Profile deleted successfully.",
                "Status": deleteProfile,
            },
            status=status.HTTP_200_OK,
        )


class GetMyProfileAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        profile = ProfileService.get_my_profile(request.user)

        serializer = ProfileSerializers(profile)

        return Response(
            {
                "message": "Profile fetched successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class GetProfileByIdAPI(APIView):
    def get(self, request):
        profile_id = request.query_params.get("profile_id")
        get_profile = ProfileService.get_profile_by_id(profile_id=profile_id)
        return Response(
            {
                "message": "Get Profile by id.",
                "data": ProfileSerializers(get_profile).data,
            },
            status=status.HTTP_200_OK,
        )


class GetAllProfileAPI(APIView):
    def get(self, request):
        profiles = ProfileService.get_all_profile()
        all_profiles = ProfileSerializers(profiles, many=True)
        return Response(
            {
                "message": "All profiles retrieved successfully.",
                "total": len(all_profiles.data),
                "data": all_profiles.data,
            },
            status=status.HTTP_200_OK,
        )


class GetActiveProfileAPI(APIView):
    def get(self, request):
        get_active_profile = ProfileService.get_active_profile()
        activated = ProfileSerializers(get_active_profile, many=True)
        return Response(
            {
                "message": "All Active Profile retrieved successfully.",
                "ActiveProfile": activated.data,
            },
            status=status.HTTP_200_OK,
        )


class GetInActiveProfileAPI(APIView):
    def get(self, request):
        get_all_inactive_profile = ProfileService.get_all_inactive_profile()
        inactive = ProfileSerializers(get_all_inactive_profile, many=True)
        return Response(
            {
                "message": "All Inactive profile retrieved successfully.",
                "total": len(inactive.data),
                "InactiveProfile": inactive.data,
            },
            status=status.HTTP_200_OK,
        )


class MakeInactiveProfileAPI(APIView):
    def post(self, request):
        profile_id = request.query_params.get("profile_id")
        makeinactiveProfile = ProfileService.make_inactive_profile(
            profile_id=profile_id
        )
        return Response(
            {
                "message": "Profile Inactive.",
                "status": makeinactiveProfile,
            },
            status=status.HTTP_200_OK,
        )


class VerifyProfileAPI(APIView):
    def post(self, request):
        profile_id = request.query_params.get("profile_id")
        verify = ProfileService.verify_profile(profile_id=profile_id)
        return Response(
            {
                "message": "Profile Verified successfully.",
                "status": verify,
            },
            status=status.HTTP_200_OK,
        )


class GetAllVerifiedProfile(APIView):
    def get(self, request):
        verified = ProfileService.get_all_verified_profile()
        get_all_verified = ProfileSerializers(verified, many=True)
        return Response(
            {
                "message": "All verified profile retrieved successfully.",
                "verified": get_all_verified.data,
            },
            status=status.HTTP_200_OK,
        )


class VerifiedPhotoVisiblityAPI(APIView):
    def post(self, request):
        profile_id = request.query_params.get("profile_id")
        photo_visiblity = ProfileService.verify_photo_visiblity(profile_id=profile_id)
        return Response(
            {
                "message": "profile visiblity verified successfully.",
                "status": ProfileSerializers(photo_visiblity).data,
            },
            status=status.HTTP_200_OK,
        )


class SearchProfilesAPI(APIView):

    def get(self, request):

        serializer = ProfileSearchSerializer(data=request.query_params)

        serializer.is_valid(raise_exception=True)

        profiles = ProfileService.search_profiles(serializer.validated_data)

        profile_serializer = ProfileSerializers(profiles, many=True)

        return Response(
            {
                "message": "Profiles retrieved successfully.",
                "data": profile_serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class UpdateProfilePhotoAPI(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, profile_id):

        photo = request.FILES.get("profile_photo")

        if not photo:
            return Response(
                {"message": "Profile photo is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        profile = ProfileService.update_profile_photo(
            profile_id=profile_id,
            user=request.user,
            photo=photo,
        )

        return Response(
            {
                "message": "Profile photo updated successfully.",
                "data": ProfileSerializers(profile).data,
            },
            status=status.HTTP_200_OK,
        )


class ProfileApprovalAPI(APIView):

    def patch(self, request):

        profile_id = request.query_params.get("profile_id")

        approved = ProfileService.approve_profile(
            profile_id=profile_id,
        )
        return Response(
            {
                "message": "Profile approved successfully.",
                "data": ProfileSerializers(approved).data,
            },
            status=status.HTTP_200_OK,
        )


class RejectProfileAPI(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request):
        profile_id = request.query_params.get("profile_id")

        profile = ProfileService.reject_profile(profile_id=profile_id)

        return Response(
            {
                "message": "Profile rejected successfully.",
                "data": ProfileSerializers(profile).data,
            },
            status=status.HTTP_200_OK,
        )
