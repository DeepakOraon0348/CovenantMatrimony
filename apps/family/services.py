from django.shortcuts import get_object_or_404

from apps.profiles.models import Profile

from .models import Family


class FamilyService:

    @staticmethod
    def create_family(
        profile_id,
        user,
        validated_data,
    ):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
            user=user,
        )

        if Family.objects.filter(
            profile=profile
        ).exists():

            raise ValueError(
                "Family details already exist for this profile."
            )

        family = Family.objects.create(
            profile=profile,
            **validated_data,
        )

        return family

    @staticmethod
    def get_my_family(profile_id, user):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
            user=user,
        )

        family = get_object_or_404(
            Family,
            profile=profile,
        )

        return family

    @staticmethod
    def update_family(
        profile_id,
        user,
        validated_data,
    ):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
            user=user,
        )

        family = get_object_or_404(
            Family,
            profile=profile,
        )

        for field, value in validated_data.items():

            setattr(
                family,
                field,
                value,
            )

        family.save()

        return family

    @staticmethod
    def delete_family(
        profile_id,
        user,
    ):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
            user=user,
        )

        family = get_object_or_404(
            Family,
            profile=profile,
        )

        family.delete()

        return True