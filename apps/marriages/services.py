from django.db import transaction
from django.core.exceptions import ValidationError
from django.db.models import Q

from apps.meetings.models import (
    Meeting,
    MeetingStatus,
)

from .models import (
    Marriage,
    MarriageStatus,
)

from .validators import (
    validate_marriage_date,
)


class MarriageService:

    # =====================================================
    # CREATE MARRIAGE
    # =====================================================

    @staticmethod
    @transaction.atomic
    def create_marriage(
        user,
        meeting,
        marriage_date,
        venue,
        pastor_name,
        remarks=None,
    ):

        # -----------------------------------------
        # Check user belongs to the meeting's match
        # -----------------------------------------

        MarriageService.validate_meeting_access(
            user=user,
            meeting=meeting,
        )

        # -----------------------------------------
        # Meeting must be completed
        # -----------------------------------------

        if meeting.status != MeetingStatus.COMPLETED:

            raise ValidationError(
                "Marriage can only be created "
                "for a completed meeting."
            )

        # -----------------------------------------
        # Check marriage already exists
        # -----------------------------------------

        if Marriage.objects.filter(
            meeting=meeting
        ).exists():

            raise ValidationError(
                "A marriage already exists "
                "for this meeting."
            )

        # -----------------------------------------
        # Validate marriage date
        # -----------------------------------------

        validate_marriage_date(
            marriage_date=marriage_date,
            meeting=meeting,
        )

        # -----------------------------------------
        # Create marriage
        # -----------------------------------------

        marriage = Marriage.objects.create(
            meeting=meeting,
            marriage_date=marriage_date,
            venue=venue,
            pastor_name=pastor_name,
            status=MarriageStatus.PENDING,
            remarks=remarks,
        )

        return marriage

    # =====================================================
    # GET ALL MARRIAGES
    # =====================================================

    @staticmethod
    def get_all_marriages():

        return Marriage.objects.select_related(
            "meeting",
            "meeting__match",
            "meeting__match__interest_request",
        ).order_by(
            "-created_at"
        )

    # =====================================================
    # GET MARRIAGE BY ID
    # =====================================================

    @staticmethod
    def get_marriage_by_id(
        marriage_id,
    ):

        try:

            return Marriage.objects.select_related(
                "meeting",
                "meeting__match",
                "meeting__match__interest_request",
            ).get(
                id=marriage_id
            )

        except Marriage.DoesNotExist:

            raise ValidationError(
                "Marriage not found."
            )

    # =====================================================
    # GET USER'S MARRIAGES
    # =====================================================

    @staticmethod
    def get_my_marriages(user):

        return Marriage.objects.filter(
        Q(
            meeting__match__interest_request__sender_profile__user=user
        )
        |
        Q(
            meeting__match__interest_request__receiver_profile__user=user
        )
    ).select_related(
        "meeting",
        "meeting__match",
        "meeting__match__interest_request",
    ).order_by(
        "-created_at"
    )
    # =====================================================
    # UPDATE MARRIAGE
    # =====================================================

    @staticmethod
    @transaction.atomic
    def update_marriage(
        user,
        marriage,
        marriage_date,
        venue,
        pastor_name,
        remarks=None,
    ):

        MarriageService.validate_marriage_access(
            user=user,
            marriage=marriage,
        )

        validate_marriage_date(
            marriage_date=marriage_date,
            meeting=marriage.meeting,
        )

        marriage.marriage_date = marriage_date
        marriage.venue = venue
        marriage.pastor_name = pastor_name
        marriage.remarks = remarks

        marriage.save()

        return marriage

    # =====================================================
    # UPDATE STATUS
    # =====================================================

    @staticmethod
    @transaction.atomic
    def update_status(
        user,
        marriage,
        status,
    ):

        MarriageService.validate_marriage_access(
            user=user,
            marriage=marriage,
        )

        marriage.status = status

        marriage.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )

        return marriage

    # =====================================================
    # DELETE MARRIAGE
    # =====================================================

    @staticmethod
    @transaction.atomic
    def delete_marriage(
        user,
        marriage,
    ):

        MarriageService.validate_marriage_access(
            user=user,
            marriage=marriage,
        )

        marriage.delete()

    # =====================================================
    # VALIDATE MEETING ACCESS
    # =====================================================

    @staticmethod
    def validate_meeting_access(
        user,
        meeting,
    ):

        interest_request = (
            meeting
            .match
            .interest_request
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
                "You do not have permission "
                "to create a marriage for this meeting."
            )

    # =====================================================
    # VALIDATE MARRIAGE ACCESS
    # =====================================================

    @staticmethod
    def validate_marriage_access(
        user,
        marriage,
    ):

        MarriageService.validate_meeting_access(
            user=user,
            meeting=marriage.meeting,
        )