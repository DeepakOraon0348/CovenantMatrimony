from django.core.exceptions import ValidationError

from apps.profiles.models import Profile

from .models import (
    InterestRequest,
    InterestRequestStatus,
    Match,
    MatchStatus,
)


def validate_profile_exists(profile_id):

    try:
        return Profile.objects.get(id=profile_id)

    except Profile.DoesNotExist:

        raise ValidationError(
            "Profile does not exist."
        )


def validate_different_profiles(
    sender_profile,
    receiver_profile,
):

    if sender_profile.id == receiver_profile.id:

        raise ValidationError(
            "You cannot send an interest request to yourself."
        )


def validate_existing_request(
    sender_profile,
    receiver_profile,
):

    existing_request = InterestRequest.objects.filter(
        sender_profile=sender_profile,
        receiver_profile=receiver_profile,
        status__in=[
            InterestRequestStatus.PENDING,
            InterestRequestStatus.ACCEPTED,
        ],
    ).first()

    if existing_request:

        raise ValidationError(
            "An interest request already exists."
        )

    reverse_request = InterestRequest.objects.filter(
        sender_profile=receiver_profile,
        receiver_profile=sender_profile,
        status__in=[
            InterestRequestStatus.PENDING,
            InterestRequestStatus.ACCEPTED,
        ],
    ).first()

    if reverse_request:

        raise ValidationError(
            "This profile has already sent you an interest request."
        )


def validate_request_receiver(
    interest_request,
    user,
):

    if interest_request.receiver_profile.user_id != user.id:

        raise ValidationError(
            "You are not allowed to respond to this request."
        )


def validate_request_sender(
    interest_request,
    user,
):

    if interest_request.sender_profile.user_id != user.id:

        raise ValidationError(
            "You are not allowed to modify this request."
        )


def validate_match_user(
    match,
    user,
):

    sender_user_id = (
        match.interest_request.sender_profile.user_id
    )

    receiver_user_id = (
        match.interest_request.receiver_profile.user_id
    )

    if user.id not in [
        sender_user_id,
        receiver_user_id,
    ]:

        raise ValidationError(
            "You are not a participant in this match."
        )


def validate_match_active(match):

    if match.status != MatchStatus.ACTIVE:

        raise ValidationError(
            "This match is already closed."
        )