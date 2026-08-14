from django.db import models
from apps.accounts.models import User
from apps.common.models import Denomination


class ProfileStatus(models.TextChoices):
    NEW = "NEW", "New"
    VERIFIED = "VERIFIED", "Verified"
    REJECTED = "REJECTED", "Rejected"
    MATCHED = "MATCHED", "Matched"
    MARRIED = "MARRIED", "Married"
    BLOCKED = "BLOCKED", "Blocked"


class Gender(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"


class MaritalStatus(models.TextChoices):
    NEVER_MARRIED = "UNMARRIED", "Unmarried"
    DIVORCED = "DIVORCED", "Divorced"
    WIDOW = "WIDOW", "Widow"
    WIDOWER = "WIDOWER", "Widower"


class ProfileType(models.TextChoices):
    BRIDE = "BRIDE", "Bride"
    GROOM = "GROOM", "Groom"


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    profile_id = models.CharField(
        max_length=20,
        unique=True,
    )

    profile_type = models.CharField(
        max_length=10,
        choices=ProfileType.choices,
    )

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
    )

    date_of_birth = models.DateField()

    denomination = models.ForeignKey(
        Denomination, on_delete=models.PROTECT, related_name="profiles"
    )

    marital_status = models.CharField(
        max_length=20,
        choices=MaritalStatus.choices,
    )

    height = models.DecimalField(
        max_digits=4,
        decimal_places=1,
    )

    weight = models.PositiveIntegerField()

    education = models.CharField(max_length=150)

    occupation = models.CharField(max_length=150)

    annual_income = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
    )

    about_me = models.TextField()

    profile_photo = models.ImageField(
        upload_to="profiles/photos/",
        blank=True,
        null=True,
    )

    is_profile_completed = models.BooleanField(default=False)

    profile_status = models.CharField(
        max_length=20,
        choices=ProfileStatus.choices,
        default=ProfileStatus.NEW,
    )

    is_photo_visible = models.BooleanField(default=False)

    is_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
