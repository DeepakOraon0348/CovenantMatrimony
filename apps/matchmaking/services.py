from django.db import transaction
from django.core.exceptions import ValidationError

from .models import (
    InterestRequest,
    InterestRequestStatus,
    Match,
    MatchStatus,
)

from .validators import (
    validate_different_profiles,
    validate_existing_request,
    validate_request_receiver,
    validate_request_sender,
    validate_match_user,
    validate_match_active,
)


class InterestRequestService:

    @staticmethod
    @transaction.atomic
    def create_interest_request(
        sender_profile,
        receiver_profile,
        message=None,
    ):

        if sender_profile == receiver_profile:

            raise ValidationError(
                "You cannot send an interest request to yourself."
            )

        existing_request = InterestRequest.objects.filter(
            sender_profile=sender_profile,
            receiver_profile=receiver_profile,
        ).first()

        if existing_request:

            raise ValidationError(
                "Interest request already exists."
            )

        interest_request = (
            InterestRequest.objects.create(
                sender_profile=sender_profile,
                receiver_profile=receiver_profile,
                message=message,
                status=InterestRequestStatus.PENDING,
            )
        )

        return interest_request


    @staticmethod
    @transaction.atomic
    def accept_interest_request(
        user,
        interest_request,
    ):

        validate_request_receiver(
            interest_request,
            user,
        )

        if (
            interest_request.status
            != InterestRequestStatus.PENDING
        ):

            raise ValidationError(
                "Only pending requests can be accepted."
            )

        interest_request.status = (
            InterestRequestStatus.ACCEPTED
        )

        interest_request.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )

        match = Match.objects.create(
            interest_request=interest_request,
            status=MatchStatus.ACTIVE,
        )

        return match


    @staticmethod
    @transaction.atomic
    def reject_interest_request(
        user,
        interest_request,
    ):

        validate_request_receiver(
            interest_request,
            user,
        )

        if (
            interest_request.status
            != InterestRequestStatus.PENDING
        ):

            raise ValidationError(
                "Only pending requests can be rejected."
            )

        interest_request.status = (
            InterestRequestStatus.REJECTED
        )

        interest_request.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )

        return interest_request


    @staticmethod
    @transaction.atomic
    def cancel_interest_request(
        user,
        interest_request,
    ):

        validate_request_sender(
            interest_request,
            user,
        )

        if (
            interest_request.status
            != InterestRequestStatus.PENDING
        ):

            raise ValidationError(
                "Only pending requests can be cancelled."
            )

        interest_request.status = (
            InterestRequestStatus.REJECTED
        )

        interest_request.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )

        return interest_request


class MatchService:

    @staticmethod
    def get_user_matches(user):

        return (
            Match.objects
            .filter(
                interest_request__sender_profile__user=user
            )
            |
            Match.objects.filter(
                interest_request__receiver_profile__user=user
            )
        ).distinct()


    @staticmethod
    @transaction.atomic
    def close_match(
        user,
        match,
    ):

        validate_match_user(
            match,
            user,
        )

        validate_match_active(
            match,
        )

        match.status = MatchStatus.CLOSED

        match.save(
            update_fields=[
                "status",
                "updated_at",
            ]
        )

        return match