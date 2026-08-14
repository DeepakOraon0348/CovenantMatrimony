from rest_framework import serializers

from .models import (
    Prayer,
    PrayerStatus,
)


class PrayerSerializer(
    serializers.ModelSerializer
):

    church_name = serializers.CharField(
        source="church.name",
        read_only=True,
    )

    created_by_name = serializers.SerializerMethodField()

    class Meta:

        model = Prayer

        fields = [
            "id",
            "church",
            "church_name",
            "created_by",
            "created_by_name",
            "title",
            "note",
            "status",
            "created_at",
            "completed_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "church",
            "church_name",
            "created_by",
            "created_by_name",
            "created_at",
            "completed_at",
            "updated_at",
        ]

    def get_created_by_name(
        self,
        obj
    ):

        if not obj.created_by:
            return None

        return (
            f"{obj.created_by.first_name} "
            f"{obj.created_by.last_name}"
        ).strip()


class CreatePrayerSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Prayer

        fields = [
            "title",
            "note",
        ]

        extra_kwargs = {
            "title": {
                "required": True,
            },
            "note": {
                "required": False,
                "allow_blank": True,
                "allow_null": True,
            },
        }


class UpdatePrayerSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Prayer

        fields = [
            "title",
            "note",
        ]


class UpdatePrayerStatusSerializer(
    serializers.Serializer
):

    status = serializers.ChoiceField(
        choices=PrayerStatus.choices
    )