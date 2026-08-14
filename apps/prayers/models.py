from django.db import models

from apps.churches.models import Church
from apps.accounts.models import User


class PrayerStatus(models.TextChoices):

    ONGOING = "ONGOING", "Ongoing"
    COMPLETED = "COMPLETED", "Completed"


class Prayer(models.Model):

    church = models.ForeignKey(
        Church,
        on_delete=models.CASCADE,
        related_name="prayers",
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_prayers",
    )

    title = models.CharField(
        max_length=255
    )

    note = models.TextField(
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=PrayerStatus.choices,
        default=PrayerStatus.ONGOING,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return (
            f"Prayer #{self.id} - "
            f"{self.title} - "
            f"{self.status}"
        )