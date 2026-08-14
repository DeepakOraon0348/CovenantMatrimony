from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.branches.models import *
from apps.churches.models import *


# Create your models here.
class UserRole(models.TextChoices):
    SUPER_ADMIN = "SUPER_ADMIN", "Super Admin"
    BRANCH_ADMIN = "BRANCH_ADMIN", "Branch Admin"
    CHURCH_ADMIN = "CHURCH_ADMIN", "Church Admin"
    USER = "USER", "User"


class User(AbstractUser):

    username = None

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=10, unique=True)

    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER,
    )

    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )

    church = models.ForeignKey(
        Church,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )

    first_name = models.CharField(
        max_length=100,
        blank=True,
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
    )

    is_email_verified = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    is_deleted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
