from django.db import models
from apps.profiles.models import Profile


class FamilyType(models.TextChoices):
    NUCLEAR = "NUCLEAR", "Nuclear"
    JOINT = "JOINT", "Joint"


class Family(models.Model):

    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name="family",
    )

    father_name = models.CharField(
        max_length=100,
    )

    mother_name = models.CharField(
        max_length=100,
    )

    father_occupation = models.CharField(
        max_length=150,
        blank=True,
    )

    mother_occupation = models.CharField(
        max_length=150,
        blank=True,
    )

    brothers = models.PositiveIntegerField(
        default=0,
    )

    sisters = models.PositiveIntegerField(
        default=0,
    )

    family_type = models.CharField(
        max_length=20,
        choices=FamilyType.choices,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"Family - {self.profile.profile_id}"