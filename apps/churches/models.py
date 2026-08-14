from django.db import models

from apps.branches.models import Branch


class Church(models.Model):

    class VerificationStatus(models.TextChoices):
        PENDING = "PENDING", "Pending"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, related_name="churches"
    )

    name = models.CharField(max_length=200)

    code = models.CharField(max_length=20, unique=True)

    pastor_name = models.CharField(max_length=150)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=10)

    address = models.TextField()

    city = models.CharField(max_length=100)

    state = models.CharField(max_length=100)

    country = models.CharField(max_length=100, default="India")

    pincode = models.CharField(max_length=6)

    description = models.TextField(blank=True)

    logo = models.ImageField(upload_to="churches/logo/", blank=True, null=True)

    verification_status = models.CharField(
        max_length=20,
        choices=VerificationStatus.choices,
        default=VerificationStatus.PENDING,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
