from rest_framework import serializers

from apps.accounts.models import User

from .models import Profile
from .validators import *
from apps.common.models import Denomination

class ProfileDenominationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Denomination
        fields = [
            "id",
            "name",
        ]

class ProfileUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
        ]

class ProfileSerializers(serializers.ModelSerializer):

    profile_id = serializers.CharField(read_only=True)
    user = ProfileUserSerializer(read_only=True)
    denomination = ProfileDenominationSerializer(read_only=True)

    height = serializers.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[validate_height],
    )

    weight = serializers.IntegerField(
        validators=[validate_weight],
    )

    education = serializers.CharField(
        validators=[validate_education],
    )

    occupation = serializers.CharField(
        validators=[validate_occupation],
    )

    annual_income = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        required=False,
        allow_null=True,
        validators=[validate_annual_income],
    )

    about_me = serializers.CharField(
        validators=[validate_about_me],
    )

    class Meta:
        model = Profile

        fields = "__all__"

        read_only_fields = (
            "profile_id",
            "is_profile_completed",
            "profile_status",
            "is_photo_visible",
            "is_verified",
            "is_active",
            "created_at",
            "updated_at",
        )


class UpdateProfileSerializer(serializers.ModelSerializer):

    height = serializers.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[validate_height],
        required=False,
    )

    weight = serializers.IntegerField(
        validators=[validate_weight],
        required=False,
    )

    education = serializers.CharField(
        validators=[validate_education],
        required=False,
    )

    occupation = serializers.CharField(
        validators=[validate_occupation],
        required=False,
    )

    annual_income = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        required=False,
        allow_null=True,
        validators=[validate_annual_income],
    )

    about_me = serializers.CharField(
        validators=[validate_about_me],
        required=False,
    )

    class Meta:
        model = Profile

        fields = "__all__"

        read_only_fields = (
            "user",
            "profile_id",
            "is_profile_completed",
            "profile_status",
            "is_photo_visible",
            "is_verified",
            "is_active",
            "created_at",
            "updated_at",
        )


class ProfileSearchSerializer(serializers.Serializer):

    gender = serializers.CharField(required=False)

    min_age = serializers.IntegerField(
        required=False,
        validators=[validate_age],
    )

    max_age = serializers.IntegerField(
        required=False,
        validators=[validate_age],
    )

    min_height = serializers.DecimalField(
        max_digits=4,
        decimal_places=1,
        required=False,
        validators=[validate_height],
    )

    max_height = serializers.DecimalField(
        max_digits=4,
        decimal_places=1,
        required=False,
        validators=[validate_height],
    )

    occupation = serializers.CharField(required=False)

    education = serializers.CharField(required=False)

    marital_status = serializers.CharField(required=False)

    denomination = serializers.IntegerField(required=False)

    min_income = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        required=False,
    )

    max_income = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        required=False,
    )
