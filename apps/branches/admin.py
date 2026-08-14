from django.contrib import admin
from .models import Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "code",
        "city",
        "state",
        "verification_status",
        "is_active",
    )

    search_fields = ("name", "code", "city")
    list_filter = ("verification_status", "state", "is_active")
