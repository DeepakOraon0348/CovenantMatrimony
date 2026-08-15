from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from apps.profiles.models import Profile

from .models import (
    InterestRequest,
    Match,
)

from .serializers import (
    InterestRequestSerializer,
    CreateInterestRequestSerializer,
    MatchSerializer,
)

from .services import (
    InterestRequestService,
    MatchService,
)


class CreateInterestRequestAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CreateInterestRequestSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        receiver_profile_id = serializer.validated_data[
            "receiver_profile"
        ]

        message = serializer.validated_data.get(
            "message"
        )

        print(
            "Receiver Profile ID:",
            receiver_profile_id
        )

        try:

            # Receiver
            receiver_profile = Profile.objects.get(
                id=receiver_profile_id
            )

            # Sender
            sender_profile = Profile.objects.get(
                user=request.user
            )

            print(
                "Sender Profile:",
                sender_profile.is_photo_visible
            )

            print(
                "Receiver Profile:",
                receiver_profile.is_photo_visible
            )
            if(sender_profile.is_photo_visible and receiver_profile.is_photo_visible):
                interest_request = (
                    InterestRequestService
                        .create_interest_request(
                        sender_profile=sender_profile,
                        receiver_profile=receiver_profile,
                        message=message,
                   )
                )
            elif(receiver_profile.is_photo_visible):
                return Response(
                    {
                        "message":"Receiver not allow to create match."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                return Response(
                    {
                        "message":"Not allow to create match.",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except Profile.DoesNotExist:

            return Response(
                {
                    "message": "Profile not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        except ValidationError as error:

            return Response(
                {
                    "message": (
                        error.message
                        if hasattr(error, "message")
                        else str(error)
                    )
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": (
                    "Interest request sent successfully."
                ),
                "data": InterestRequestSerializer(
                    interest_request
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )


class GetSentInterestRequestsAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        requests = (
            InterestRequest.objects
            .filter(
                sender_profile__user=request.user
            )
            .order_by("-created_at")
        )

        serializer = InterestRequestSerializer(
            requests,
            many=True
        )

        return Response(
            {
                "message": (
                    "Sent interest requests fetched successfully."
                ),
                "total": requests.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class GetReceivedInterestRequestsAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        requests = (
            InterestRequest.objects
            .filter(
                receiver_profile__user=request.user
            )
            .order_by("-created_at")
        )

        serializer = InterestRequestSerializer(
            requests,
            many=True
        )

        return Response(
            {
                "message": (
                    "Received interest requests fetched successfully."
                ),
                "data": serializer.data,
                "total": requests.count(),
            },
            status=status.HTTP_200_OK,
        )


class GetInterestRequestAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):
        interest_id = request.query_params.get(
            "interest_id"
        )

        try:

            interest_request = (
                InterestRequest.objects
                .get(id=interest_id)
            )

        except InterestRequest.DoesNotExist:

            return Response(
                {
                    "message": (
                        "Interest request not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        if request.user.id not in [
            interest_request.sender_profile.user_id,
            interest_request.receiver_profile.user_id,
        ]:

            return Response(
                {
                    "message": "Permission denied."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = InterestRequestSerializer(
            interest_request
        )

        return Response(
            {
                "message": (
                    "Interest request fetched successfully."
                ),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class AcceptInterestRequestAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):
        interest_id=request.query_params.get("interest_id")
        if not interest_id:
            return Response(
                {
                    "message": "interest_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:

            interest_request = (
                InterestRequest.objects
                .select_related(
                    "sender_profile__user",
                    "receiver_profile__user",
                )
                .get(id=interest_id)
            )

        except InterestRequest.DoesNotExist:

            return Response(
                {
                    "message": (
                        "Interest request not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:

            match = (
                InterestRequestService
                .accept_interest_request(
                    user=request.user,
                    interest_request=interest_request,
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
                    "Interest request accepted "
                    "and match created successfully."
                ),
                "data": MatchSerializer(
                    match
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class RejectInterestRequestAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):
        intrest_id=request.query_params.get("intrest_id")

        try:

            interest_request = (
                InterestRequest.objects.get(
                    id=intrest_id
                )
            )

        except InterestRequest.DoesNotExist:

            return Response(
                {
                    "message": (
                        "Interest request not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:

            interest_request = (
                InterestRequestService
                .reject_interest_request(
                    user=request.user,
                    interest_request=interest_request,
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
                    "Interest request rejected successfully."
                ),
                "data": InterestRequestSerializer(
                    interest_request
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class CancelInterestRequestAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):
        interest_id=request.query_params.get("interest_id")
        try:

            interest_request = (
                InterestRequest.objects.get(
                    id=interest_id
                )
            )

        except InterestRequest.DoesNotExist:

            return Response(
                {
                    "message": (
                        "Interest request not found."
                    )
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:

            interest_request = (
                InterestRequestService
                .cancel_interest_request(
                    user=request.user,
                    interest_request=interest_request,
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
                    "Interest request cancelled successfully."
                ),
                "data": InterestRequestSerializer(
                    interest_request
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class GetMyMatchesAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        matches = MatchService.get_user_matches(
            request.user
        )

        serializer = MatchSerializer(
            matches,
            many=True
        )

        return Response(
            {
                "message": (
                    "Matches fetched successfully."
                ),
                "data": serializer.data,
                "total": matches.count(),
            },
            status=status.HTTP_200_OK,
        )


class GetMatchAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):
        match_id=request.query_params.get("match_id")

        try:

            match = (
                Match.objects
                .select_related(
                    "interest_request__sender_profile__user",
                    "interest_request__receiver_profile__user",
                )
                .get(id=match_id)
            )

        except Match.DoesNotExist:

            return Response(
                {
                    "message": "Match not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        sender_user_id = (
            match.interest_request
            .sender_profile.user_id
        )

        receiver_user_id = (
            match.interest_request
            .receiver_profile.user_id
        )

        if request.user.id not in [
            sender_user_id,
            receiver_user_id,
        ]:

            return Response(
                {
                    "message": "Permission denied."
                },
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = MatchSerializer(
            match
        )

        return Response(
            {
                "message": "Match fetched successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class CloseMatchAPI(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):
        match_id=request.query_params.get("match_id")

        try:

            match = (
                Match.objects
                .select_related(
                    "interest_request__sender_profile",
                    "interest_request__receiver_profile",
                )
                .get(id=match_id)
            )

        except Match.DoesNotExist:

            return Response(
                {
                    "message": "Match not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:

            match = MatchService.close_match(
                user=request.user,
                match=match,
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
                    "Match closed successfully."
                ),
                "data": MatchSerializer(
                    match
                ).data,
            },
            status=status.HTTP_200_OK,
        )