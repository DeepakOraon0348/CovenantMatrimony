import code

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .services import *


class CreateDenominationAPI(APIView):
    def post(self, request):
        serializer = DenominatoinSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        created_denomination = DenominationService.create_denomination(
            serializer.validated_data
        )
        return Response(
            {
                "message": "Denomination created successfully.",
                "data": DenominatoinSerializers(created_denomination).data,
            },
            status=status.HTTP_201_CREATED,
        )


class GetAllDenominationAPI(APIView):
    def get(self, request):
        get_all_denomination = DenominationService.get_all_denomination()
        serializer = DenominatoinSerializers(get_all_denomination, many=True)

        return Response(
            {
                "message": "Get All Denomination List.",
                "tatal": len(serializer.data),
                "data": serializer.data,
            }
        )
