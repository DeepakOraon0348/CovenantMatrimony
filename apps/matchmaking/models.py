from django.db import models
from django.core.exceptions import ValidationError

from apps.profiles.models import Profile


class InterestRequestStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    REJECTED = "REJECTED", "Rejected"


class MatchStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    CLOSED = "CLOSED", "Closed"


class InterestRequest(models.Model):

    sender_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="sent_interest_requests",
    )

    receiver_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="received_interest_requests",
    )

    status = models.CharField(
        max_length=20,
        choices=InterestRequestStatus.choices,
        default=InterestRequestStatus.PENDING,
    )

    message = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def clean(self):
        if self.sender_profile == self.receiver_profile:
            raise ValidationError(
                "You cannot send an interest request to yourself."
            )

    def __str__(self):
        return (
            f"{self.sender_profile} -> "
            f"{self.receiver_profile} "
            f"({self.status})"
        )


class Match(models.Model):

    interest_request = models.OneToOneField(
        InterestRequest,
        on_delete=models.CASCADE,
        related_name="match",
    )

    status = models.CharField(
        max_length=20,
        choices=MatchStatus.choices,
        default=MatchStatus.ACTIVE,
    )

    matched_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return (
            f"Match #{self.id} - "
            f"{self.interest_request.sender_profile} & "
            f"{self.interest_request.receiver_profile}"
        )