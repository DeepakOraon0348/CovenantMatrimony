from rest_framework import serializers

from .models import Family
from .validators import (
    validate_name,
    validate_occupation,
    validate_siblings,
)


class FamilySerializer(serializers.ModelSerializer):

    father_name = serializers.CharField(
        validators=[validate_name],
    )

    mother_name = serializers.CharField(
        validators=[validate_name],
    )

    father_occupation = serializers.CharField(
        required=False,
        allow_blank=True,
        validators=[validate_occupation],
    )

    mother_occupation = serializers.CharField(
        required=False,
        allow_blank=True,
        validators=[validate_occupation],
    )

    brothers = serializers.IntegerField(
        validators=[validate_siblings],
    )

    sisters = serializers.IntegerField(
        validators=[validate_siblings],
    )

    class Meta:
        model = Family
        fields = "__all__"

        read_only_fields = (
            "id",
            "profile",
            "created_at",
            "updated_at",
        )