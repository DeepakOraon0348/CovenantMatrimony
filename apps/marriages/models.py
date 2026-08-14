from django.db import models

from apps.meetings.models import Meeting


class MarriageStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    COMPLETED = "COMPLETED", "Completed"


class Marriage(models.Model):

    meeting = models.OneToOneField(
        Meeting,
        on_delete=models.CASCADE,
        related_name="marriage",
    )

    marriage_date = models.DateField()

    venue = models.CharField(
        max_length=255
    )

    pastor_name = models.CharField(
        max_length=255
    )

    status = models.CharField(
        max_length=20,
        choices=MarriageStatus.choices,
        default=MarriageStatus.PENDING,
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
            f"Marriage #{self.id} - "
            f"Meeting #{self.meeting_id} - "
            f"{self.status}"
        )