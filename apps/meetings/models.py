from django.db import models

from apps.matchmaking.models import Match


class MeetingStatus(models.TextChoices):
    SCHEDULED = "SCHEDULED", "Scheduled"
    COMPLETED = "COMPLETED", "Completed"
    CANCELLED = "CANCELLED", "Cancelled"


class Meeting(models.Model):

    match = models.OneToOneField(
        Match,
        on_delete=models.CASCADE,
        related_name="meeting",
    )

    meeting_date = models.DateField()

    meeting_time = models.TimeField()

    venue = models.CharField(
        max_length=255
    )

    status = models.CharField(
        max_length=20,
        choices=MeetingStatus.choices,
        default=MeetingStatus.SCHEDULED,
    )

    remarks = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return (
            f"Meeting #{self.id} - "
            f"Match #{self.match_id} - "
            f"{self.status}"
        )