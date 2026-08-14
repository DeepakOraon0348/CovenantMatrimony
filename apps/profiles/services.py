from .models import Profile, ProfileStatus
from datetime import date
from django.shortcuts import get_object_or_404


class ProfileService:
    @staticmethod
    def create_Profile(validated_data):
        profile = Profile.objects.create(**validated_data)

        profile.profile_id = f"MAT{profile.id:06d}"

        profile.save(update_fields=["profile_id"])

        return profile

    @staticmethod
    def update_profile(profile_id, validated_data):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
        )

        for key, value in validated_data.items():
            setattr(profile, key, value)

        profile.save()

        return profile

    @staticmethod
    def delete_profile(profile_id):
        profile = get_object_or_404(
            Profile,
            id=profile_id,
        )

        profile.delete()

        return True

    @staticmethod
    def get_my_profile(user):
        """
        Get logged in user's profile.
        """
        profile = get_object_or_404(
            Profile,
            user=user,
            is_active=True,
        )

        return profile

    @staticmethod
    def get_profile_by_id(profile_id):
        profile = get_object_or_404(Profile, id=profile_id)
        return profile

    @staticmethod
    def get_all_profile():
        profiles = Profile.objects.all()
        return profiles

    @staticmethod
    def get_active_profile():
        active = get_object_or_404(Profile, is_active=True)
        return active

    @staticmethod
    def get_all_inactive_profile():
        inactive = Profile.objects.filter(is_active=False)
        return inactive

    @staticmethod
    def make_inactive_profile(profile_id):
        makeinactive = get_object_or_404(Profile, id=profile_id)
        makeinactive.is_active = False
        makeinactive.save()
        return True

    @staticmethod
    def verify_profile(profile_id):
        verify = get_object_or_404(Profile, id=profile_id)
        verify.is_verified = True
        verify.save()
        return True

    @staticmethod
    def get_all_verified_profile():
        verified = Profile.objects.filter(is_verified=True)
        return verified

    @staticmethod
    def verify_photo_visiblity(profile_id):
        verified_photo_visiblity = get_object_or_404(Profile, id=profile_id)
        verified_photo_visiblity.is_photo_visible = True
        verified_photo_visiblity.save()
        return verified_photo_visiblity

    @staticmethod
    def search_profiles(validated_data):

        profiles = Profile.objects.filter(
            is_active=True,
            is_verified=True,
        )

        # Gender
        gender = validated_data.get("gender")

        if gender:
            profiles = profiles.filter(gender__iexact=gender)

        # Occupation
        occupation = validated_data.get("occupation")

        if occupation:
            profiles = profiles.filter(occupation__icontains=occupation)

        # Education
        education = validated_data.get("education")

        if education:
            profiles = profiles.filter(education__icontains=education)

        # Marital Status
        marital_status = validated_data.get("marital_status")

        if marital_status:
            profiles = profiles.filter(marital_status=marital_status)

        # Denomination
        denomination = validated_data.get("denomination")

        if denomination:
            profiles = profiles.filter(denomination_id=denomination)

        # Height
        min_height = validated_data.get("min_height")

        if min_height:
            profiles = profiles.filter(height__gte=min_height)

        max_height = validated_data.get("max_height")

        if max_height:
            profiles = profiles.filter(height__lte=max_height)

        # Income
        min_income = validated_data.get("min_income")

        if min_income:
            profiles = profiles.filter(annual_income__gte=min_income)

        max_income = validated_data.get("max_income")

        if max_income:
            profiles = profiles.filter(annual_income__lte=max_income)

        # Age
        min_age = validated_data.get("min_age")
        max_age = validated_data.get("max_age")

        today = date.today()

        if max_age:
            min_birth_date = date(
                today.year - max_age - 1,
                today.month,
                today.day,
            )

            profiles = profiles.filter(date_of_birth__gt=min_birth_date)

        if min_age:
            max_birth_date = date(
                today.year - min_age,
                today.month,
                today.day,
            )

            profiles = profiles.filter(date_of_birth__lte=max_birth_date)

        return profiles

    @staticmethod
    def update_profile_photo(profile_id, user, photo):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
            user=user,
        )

        profile.profile_photo = photo

        profile.save(
            update_fields=[
                "profile_photo",
                "updated_at",
            ]
        )

        return profile

    @staticmethod
    def approve_profile(profile_id):

        profile = get_object_or_404(Profile, id=profile_id)

        profile.profile_status = ProfileStatus.VERIFIED
        profile.is_verified = True

        # Keep False until payment is approved
        profile.is_photo_visible = False

        profile.save(
            update_fields=[
                "profile_status",
                "is_verified",
                "is_photo_visible",
                "updated_at",
            ]
        )

        return profile

    @staticmethod
    def reject_profile(profile_id):

        profile = get_object_or_404(Profile, id=profile_id)

        profile.profile_status = ProfileStatus.REJECTED
        profile.is_verified = False
        profile.is_photo_visible = False

        profile.save(
            update_fields=[
                "profile_status",
                "is_verified",
                "is_photo_visible",
                "updated_at",
            ]
        )

        return profile
