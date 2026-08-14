from rest_framework import serializers

from .models import (
    InterestRequest,
    Match,
)


class InterestRequestSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = InterestRequest

        fields = [
            "id",
            "sender_profile",
            "receiver_profile",
            "status",
            "message",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "sender_profile",
            "status",
            "created_at",
            "updated_at",
        ]


class CreateInterestRequestSerializer(
    serializers.Serializer
):

    receiver_profile = serializers.IntegerField()

    message = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True,
    )


class InterestRequestResponseSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = InterestRequest

        fields = [
            "id",
            "sender_profile",
            "receiver_profile",
            "status",
            "message",
            "created_at",
            "updated_at",
        ]


class MatchSerializer(
    serializers.ModelSerializer
):

    interest_request = InterestRequestResponseSerializer(
        read_only=True
    )

    class Meta:

        model = Match

        fields = [
            "id",
            "interest_request",
            "status",
            "matched_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "interest_request",
            "status",
            "matched_at",
            "updated_at",
        ]