from django.core.exceptions import ValidationError

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.matchmaking.models import Match

from .models import Meeting
from .serializers import (
    MeetingSerializer,
    CreateMeetingSerializer,
    UpdateMeetingSerializer,
)
from .services import MeetingService


class CreateMeetingAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = CreateMeetingSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        # IMPORTANT:
        # This is already a Match object
        match = serializer.validated_data["match"]

        meeting_date = serializer.validated_data[
            "meeting_date"
        ]

        meeting_time = serializer.validated_data[
            "meeting_time"
        ]

        venue = serializer.validated_data[
            "venue"
        ]

        remarks = serializer.validated_data.get(
            "remarks"
        )

        try:

            meeting = MeetingService.create_meeting(
                user=request.user,
                match=match,
                meeting_date=meeting_date,
                meeting_time=meeting_time,
                venue=venue,
                remarks=remarks,
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
                    "Meeting scheduled successfully."
                ),
                "data": MeetingSerializer(
                    meeting
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )
    
    
class GetAllMeetingAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            meeting=MeetingService.get_all_meeting()
        except ValueError as error:
            return Response(
                {
                    "message":str(error),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        serializer = MeetingSerializer(
            meeting,
            many=True
        )

        return Response(
            {
                "message": "All meetings retrieved successfully.",
                "total": meeting.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
class GetMyMeetingsAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        meetings = (
            Meeting.objects.filter(
                match__interest_request__sender_profile__user=request.user
            )
            | Meeting.objects.filter(
                match__interest_request__receiver_profile__user=request.user
            )
        )

        meetings = (
            meetings
            .select_related(
                "match",
                "match__interest_request",
                "match__interest_request__sender_profile",
                "match__interest_request__receiver_profile",
            )
            .distinct()
            .order_by("-created_at")
        )

        return Response(
            {
                "message": "Meetings fetched successfully.",
                "total": meetings.count(),
                "data": MeetingSerializer(
                    meetings,
                    many=True,
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class GetMeetingAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        meeting_id = request.query_params.get(
            "meeting_id"
        )

        if not meeting_id:

            return Response(
                {
                    "message": "meeting_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            meeting = (
                Meeting.objects
                .select_related(
                    "match__interest_request__sender_profile__user",
                    "match__interest_request__receiver_profile__user",
                )
                .get(
                    id=meeting_id
                )
            )

        except Meeting.DoesNotExist:

            return Response(
                {
                    "message": "Meeting not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:

            MeetingService.get_meeting(
                user=request.user,
                meeting=meeting,
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
                "message": "Meeting fetched successfully.",
                "data": MeetingSerializer(
                    meeting
                ).data,
            },
            status=status.HTTP_200_OK,
        )


class UpdateMeetingAPI(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request):

        meeting_id = request.query_params.get(
            "meeting_id"
        )

        if not meeting_id:

            return Response(
                {
                    "message": "meeting_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            meeting = (
                Meeting.objects
                .select_related(
                    "match__interest_request__sender_profile__user",
                    "match__interest_request__receiver_profile__user",
                )
                .get(
                    id=meeting_id
                )
            )

        except Meeting.DoesNotExist:

            return Response(
                {
                    "message": "Meeting not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = UpdateMeetingSerializer(
            meeting,
            data=request.data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True
        )

        try:

            meeting = MeetingService.update_meeting(
                user=request.user,
                meeting=meeting,
                meeting_date=serializer.validated_data.get(
                    "meeting_date"
                ),
                meeting_time=serializer.validated_data.get(
                    "meeting_time"
                ),
                venue=serializer.validated_data.get(
                    "venue"
                ),
                status=serializer.validated_data.get(
                    "status"
                ),
                remarks=serializer.validated_data.get(
                    "remarks"
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
                "message": "Meeting updated successfully.",
                "data": MeetingSerializer(
                    meeting
                ).data,
            },
            status=status.HTTP_200_OK,
        )

class MeetingCompleteAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        meeting_id=request.query_params.get("meeting_id")
        if not meeting_id:
            return Response(
                {
                    "message":"Meeting id required.",
                },
                status=status.HTTP_200_OK,
            )
            
        try:
            complete_meeting=MeetingService.complete_meeting(meeting_id=meeting_id)
            
        except ValueError as error:
            return Response(
                {
                    "message":str(error),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
            
         
        return Response(
            {
                "message":"Meeting status Update successfully.",
                "data":MeetingSerializer(complete_meeting).data,
            },
            status=status.HTTP_200_OK,
        )
class CancelMeetingAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        meeting_id = request.query_params.get(
            "meeting_id"
        )

        if not meeting_id:

            return Response(
                {
                    "message": "meeting_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            meeting = (
                Meeting.objects
                .select_related(
                    "match__interest_request__sender_profile__user",
                    "match__interest_request__receiver_profile__user",
                )
                .get(
                    id=meeting_id
                )
            )

        except Meeting.DoesNotExist:

            return Response(
                {
                    "message": "Meeting not found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:

            meeting = MeetingService.cancel_meeting(
                user=request.user,
                meeting=meeting,
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
                "message": "Meeting cancelled successfully.",
                "data": MeetingSerializer(
                    meeting
                ).data,
            },
            status=status.HTTP_200_OK,
        )