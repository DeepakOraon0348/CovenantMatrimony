from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import (
    Prayer,
    PrayerStatus,
)


class PrayerService:

    # ==========================================================
    # GET USER'S CHURCH
    # ==========================================================

    @staticmethod
    def get_user_church(user):

        try:

            church = user.church

        except Exception:

            church = None

        if not church:

            raise ValidationError(
                "You are not associated with a church."
            )

        return church

    # ==========================================================
    # CREATE PRAYER
    # ==========================================================

    @staticmethod
    @transaction.atomic
    def create_prayer(
        user,
        title,
        note=None,
    ):

        church = PrayerService.get_user_church(
            user
        )

        prayer = Prayer.objects.create(
            church=church,
            created_by=user,
            title=title,
            note=note,
            status=PrayerStatus.ONGOING,
        )

        return prayer

    # ==========================================================
    # GET ALL PRAYERS
    # ==========================================================

    @staticmethod
    def get_all_prayers():

        return (
            Prayer.objects
            .select_related(
                "church",
                "created_by",
            )
            .order_by("-created_at")
        )

    # ==========================================================
    # GET PRAYERS OF LOGGED-IN USER'S CHURCH
    # ==========================================================

    @staticmethod
    def get_my_church_prayers(
        user
    ):

        church = PrayerService.get_user_church(
            user
        )

        return (
            Prayer.objects
            .filter(church=church)
            .select_related(
                "church",
                "created_by",
            )
            .order_by("-created_at")
        )

    # ==========================================================
    # GET PRAYER BY ID
    # ==========================================================

    @staticmethod
    def get_prayer_by_id(
        prayer_id
    ):

        try:

            return (
                Prayer.objects
                .select_related(
                    "church",
                    "created_by",
                )
                .get(
                    id=prayer_id
                )
            )

        except Prayer.DoesNotExist:

            raise ValidationError(
                "Prayer not found."
            )

    # ==========================================================
    # CHECK PRAYER ACCESS
    # ==========================================================

    @staticmethod
    def validate_prayer_access(
        user,
        prayer,
    ):

        church = PrayerService.get_user_church(
            user
        )

        if prayer.church_id != church.id:

            raise ValidationError(
                "You do not have permission to access this prayer."
            )

    # ==========================================================
    # UPDATE PRAYER
    # ==========================================================

    @staticmethod
    @transaction.atomic
    def update_prayer(
        user,
        prayer,
        title=None,
        note=None,
    ):

        PrayerService.validate_prayer_access(
            user=user,
            prayer=prayer,
        )

        if title is not None:

            prayer.title = title

        if note is not None:

            prayer.note = note

        prayer.save(
            update_fields=[
                "title",
                "note",
                "updated_at",
            ]
        )

        return prayer

    # ==========================================================
    # UPDATE PRAYER STATUS
    # ==========================================================

    @staticmethod
    @transaction.atomic
    def update_status(
        user,
        prayer,
        status,
    ):

        PrayerService.validate_prayer_access(
            user=user,
            prayer=prayer,
        )

        if status == PrayerStatus.COMPLETED:

            prayer.status = (
                PrayerStatus.COMPLETED
            )

            prayer.completed_at = (
                timezone.now()
            )

        elif status == PrayerStatus.ONGOING:

            prayer.status = (
                PrayerStatus.ONGOING
            )

            prayer.completed_at = None

        prayer.save(
            update_fields=[
                "status",
                "completed_at",
                "updated_at",
            ]
        )

        return prayer

    # ==========================================================
    # DELETE PRAYER
    # ==========================================================

    @staticmethod
    @transaction.atomic
    def delete_prayer(
        user,
        prayer,
    ):

        PrayerService.validate_prayer_access(
            user=user,
            prayer=prayer,
        )

        prayer.delete()