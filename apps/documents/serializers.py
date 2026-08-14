from rest_framework import serializers

from .models import Document
from .validators import validate_document_file


class DocumentSerializer(serializers.ModelSerializer):

    aadhaar = serializers.FileField(
        required=False,
        allow_null=True,
        validators=[validate_document_file],
    )

    baptism_certificate = serializers.FileField(
        required=False,
        allow_null=True,
        validators=[validate_document_file],
    )

    education_certificate = serializers.FileField(
        required=False,
        allow_null=True,
        validators=[validate_document_file],
    )

    income_certificate = serializers.FileField(
        required=False,
        allow_null=True,
        validators=[validate_document_file],
    )

    other_document = serializers.FileField(
        required=False,
        allow_null=True,
        validators=[validate_document_file],
    )

    class Meta:
        model = Document

        fields = "__all__"

        read_only_fields = (
            "id",
            "profile",  # <-- ADD THIS
            "aadhaar_status",
            "baptism_certificate_status",
            "education_certificate_status",
            "income_certificate_status",
            "other_document_status",
            "created_at",
            "updated_at",
        )