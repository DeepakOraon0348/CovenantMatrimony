from django.core.exceptions import ValidationError
from django.db import transaction

from .models import (
    Meeting,
    MeetingStatus,
)

from apps.matchmaking.models import Match


class MeetingService:

    @staticmethod
    def validate_match_access(
        user,
        match,
    ):

        interest_request = (
            match.interest_request
        )

        sender_user_id = (
            interest_request
            .sender_profile
            .user_id
        )

        receiver_user_id = (
            interest_request
            .receiver_profile
            .user_id
        )

        if user.id not in [
            sender_user_id,
            receiver_user_id,
        ]:

            raise ValidationError(
                "You are not allowed to access this match."
            )

    @staticmethod
    @transaction.atomic
    def create_meeting(
        user,
        match,
        meeting_date,
        meeting_time,
        venue,
        remarks=None,
    ):

        # -----------------------------------------
        # Check user belongs to this match
        # -----------------------------------------

        MeetingService.validate_match_access(
            user=user,
            match=match,
        )

        # -----------------------------------------
        # Match must be active
        # -----------------------------------------

        if match.status != "ACTIVE":

            raise ValidationError(
                "Meeting can only be created for an active match."
            )

        # -----------------------------------------
        # Check meeting already exists
        # -----------------------------------------

        if Meeting.objects.filter(
            match=match
        ).exists():

            raise ValidationError(
                "A meeting already exists for this match."
            )

        # -----------------------------------------
        # Create meeting
        # -----------------------------------------

        meeting = Meeting.objects.create(
            match=match,
            meeting_date=meeting_date,
            meeting_time=meeting_time,
            venue=venue,
            status=MeetingStatus.SCHEDULED,
            remarks=remarks,
        )

        return meeting


    @staticmethod
    def get_all_meeting():
        return Meeting.objects.all();
    @staticmethod
    def get_meeting(
        user,
        meeting,
    ):

        MeetingService.validate_match_access(
            user=user,
            match=meeting.match,
        )

        return meeting

    @staticmethod
    @transaction.atomic
    def update_meeting(
        user,
        meeting,
        meeting_date=None,
        meeting_time=None,
        venue=None,
        status=None,
        remarks=None,
    ):

        MeetingService.validate_match_access(
            user=user,
            match=meeting.match,
        )

        if meeting.status == MeetingStatus.CANCELLED:

            raise ValidationError(
                "Cancelled meetings cannot be updated."
            )

        if meeting_date is not None:
            meeting.meeting_date = meeting_date

        if meeting_time is not None:
            meeting.meeting_time = meeting_time

        if venue is not None:
            meeting.venue = venue

        if status is not None:
            meeting.status = status

        if remarks is not None:
            meeting.remarks = remarks

        meeting.save()

        return meeting
    
    @staticmethod
    @transaction.atomic
    def complete_meeting(meeting_id):
        meeting=Meeting.objects.filter(id=meeting_id).first()
        meeting.status= MeetingStatus.COMPLETED
        meeting.save();
        return meeting

    @staticmethod
    @transaction.atomic
    def cancel_meeting(
        user,
        meeting,
    ):

        MeetingService.validate_match_access(
            user=user,
            match=meeting.match,
        )

        if meeting.status == MeetingStatus.COMPLETED:

            raise ValidationError(
                "Completed meetings cannot be cancelled."
            )

        meeting.status = (
            MeetingStatus.CANCELLED
        )

        meeting.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )

        return meeting