from rest_framework import serializers

from .models import Meeting


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting

        fields = [
            "id",
            "match",
            "meeting_date",
            "meeting_time",
            "venue",
            "status",
            "remarks",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]


class CreateMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = [
            "match",
            "meeting_date",
            "meeting_time",
            "venue",
            "remarks",
        ]


class UpdateMeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting

        fields = [
            "meeting_date",
            "meeting_time",
            "venue",
            "status",
            "remarks",
        ]