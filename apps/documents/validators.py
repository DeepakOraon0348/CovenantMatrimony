import os
from rest_framework import serializers


ALLOWED_EXTENSIONS = [
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
]

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB


def validate_document_file(value):

    if not value:
        return value

    extension = os.path.splitext(value.name)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise serializers.ValidationError(
            "Only PDF, JPG, JPEG and PNG files are allowed."
        )

    if value.size > MAX_FILE_SIZE:
        raise serializers.ValidationError(
            "File size must not exceed 5 MB."
        )

    return value