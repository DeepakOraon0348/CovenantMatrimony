from django.db import models
from apps.profiles.models import Profile


class DocumentStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    APPROVED = "APPROVED", "Approved"
    REJECTED = "REJECTED", "Rejected"


class Document(models.Model):

    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name="document",
    )

    aadhaar = models.FileField(
        upload_to="profiles/documents/aadhaar/",
        blank=True,
        null=True,
    )

    aadhaar_status = models.CharField(
        max_length=20,
        choices=DocumentStatus.choices,
        default=DocumentStatus.PENDING,
    )

    baptism_certificate = models.FileField(
        upload_to="profiles/documents/baptism/",
        blank=True,
        null=True,
    )

    baptism_certificate_status = models.CharField(
        max_length=20,
        choices=DocumentStatus.choices,
        default=DocumentStatus.PENDING,
    )

    education_certificate = models.FileField(
        upload_to="profiles/documents/education/",
        blank=True,
        null=True,
    )

    education_certificate_status = models.CharField(
        max_length=20,
        choices=DocumentStatus.choices,
        default=DocumentStatus.PENDING,
    )

    income_certificate = models.FileField(
        upload_to="profiles/documents/income/",
        blank=True,
        null=True,
    )

    income_certificate_status = models.CharField(
        max_length=20,
        choices=DocumentStatus.choices,
        default=DocumentStatus.PENDING,
    )

    other_document = models.FileField(
        upload_to="profiles/documents/other/",
        blank=True,
        null=True,
    )

    other_document_status = models.CharField(
        max_length=20,
        choices=DocumentStatus.choices,
        default=DocumentStatus.PENDING,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"Document - {self.profile.profile_id}"