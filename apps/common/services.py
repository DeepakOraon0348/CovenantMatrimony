from django.shortcuts import get_object_or_404
from .models import Denomination


class DenominationService:
    @staticmethod
    def create_denomination(validated_data):
        denomination = Denomination.objects.create(**validated_data)
        return denomination

    @staticmethod
    def get_all_denomination():
        return Denomination.objects.all()
