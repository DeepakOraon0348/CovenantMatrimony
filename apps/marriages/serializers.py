from rest_framework import serializers

from .models import Marriage


class MarriageSerializer(serializers.ModelSerializer):

    class Meta:

        model = Marriage

        fields = [
            "id",
            "meeting",
            "marriage_date",
            "venue",
            "pastor_name",
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


class CreateMarriageSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Marriage

        fields = [
            "meeting",
            "marriage_date",
            "venue",
            "pastor_name",
            "remarks",
        ]


class UpdateMarriageSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Marriage

        fields = [
            "marriage_date",
            "venue",
            "pastor_name",
            "remarks",
        ]


class UpdateMarriageStatusSerializer(
    serializers.Serializer
):

    status = serializers.ChoiceField(
        choices=Marriage._meta.get_field(
            "status"
        ).choices
    )