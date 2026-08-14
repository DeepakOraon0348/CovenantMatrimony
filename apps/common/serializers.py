from rest_framework import serializers
from .models import *

from .validators import *


class DenominatoinSerializers(serializers.ModelSerializer):
    name = serializers.CharField(validators=[validate_name])

    class Meta:
        model = Denomination
        fields = "__all__"
