import code

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .services import *


# Create your views here.
class CreateChurchAPI(APIView):
    def post(self, request):
        serializer = CreateChurchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        created_church = ChurchService.create_church(serializer.validated_data)
        return Response(
            {
                "message": "Church created successfully.",
                "data": CreateChurchSerializer(created_church).data,
            },
            status=status.HTTP_201_CREATED,
        )


class UpdateChurchAPI(APIView):
    def post(self, request, church_id):
        serializer = UpdateChurchSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_church = ChurchService.update_church(
            church_id=church_id,
            validated_data=serializer.validated_data,
        )

        return Response(
            {
                "message": "Church updated successfully.",
                "data": CreateChurchSerializer(updated_church).data,
            },
            status=status.HTTP_200_OK,
        )


class GetAllChurchesAPI(APIView):
    def get(self, request):
        churches = ChurchService.get_all_churches()
        serializer = CreateChurchSerializer(churches, many=True)
        return Response(
            {
                "message": "All churches retrieved successfully.",
                "total": churches.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class GetChurchByIdAPI(APIView):
    def get(self, request):
        church_id = request.query_params.get("church_id")
        if not church_id:
            return Response(
                {"message": "church_id query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        church = ChurchService.get_church_by_id(church_id=church_id)
        serializer = CreateChurchSerializer(church)
        return Response(
            {
                "message": "Church retrieved successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class DeleteChurchAPI(APIView):
    def delete(self, request):
        church_id = request.query_params.get("church_id")
        if not church_id:
            return Response(
                {"message": "church_id query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        church = ChurchService.delete_church(church_id=church_id)
        return Response(
            {"message": "Church deleted successfully.", "status": church},
            status=status.HTTP_200_OK,
        )


class ApproveChurchAPI(APIView):
    def post(self, request):
        church_id = request.query_params.get("church_id")
        if not church_id:
            return Response(
                {"message": "church_id query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        church = ChurchService.approve_church(church_id=church_id)
        return Response(
            {
                "message": "Church approved successfully.",
                "data": CreateChurchSerializer(church).data,
            },
            status=status.HTTP_200_OK,
        )


class RejectChurchAPI(APIView):
    def post(self, request):
        church_id = request.query_params.get("church_id")
        if not church_id:
            return Response(
                {"message": "church_id query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        church = ChurchService.reject_church(church_id=church_id)
        return Response(
            {
                "message": "Church rejected successfully.",
                "data": CreateChurchSerializer(church).data,
            },
            status=status.HTTP_200_OK,
        )


class GetApprovedChurchesAPI(APIView):
    def get(self, request):
        approved_churches = ChurchService.get_approved_churches()
        serializer = CreateChurchSerializer(approved_churches, many=True)
        return Response(
            {
                "message": "Approved churches retrieved successfully.",
                "total": approved_churches.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class GetAllRejectedChurchesAPI(APIView):
    def get(self, request):
        rejected_churches = ChurchService.get_all_rejected_churches()
        serializer = CreateChurchSerializer(rejected_churches, many=True)
        return Response(
            {
                "message": "Rejected churches retrieved successfully.",
                "total": rejected_churches.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class GetAllPendingChurchesAPI(APIView):

    def get(self, request):
        pending_churches = ChurchService.get_all_pending_churches()
        serializer = CreateChurchSerializer(pending_churches, many=True)
        return Response(
            {
                "message": "Pending churches retrieved successfully.",
                "total": pending_churches.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class ActivateChurchAPI(APIView):
    def post(self, request):
        church_id = request.query_params.get("church_id")
        if not church_id:
            return Response(
                {"message": "church_id query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        church = ChurchService.activate_church(church_id=church_id)
        return Response(
            {
                "message": "Church activated successfully.",
                "data": CreateChurchSerializer(church).data,
            },
            status=status.HTTP_200_OK,
        )


class DeactivateChurchAPI(APIView):
    def post(self, request):
        church_id = request.query_params.get("church_id")
        if not church_id:
            return Response(
                {"message": "church_id query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        church = ChurchService.deactivate_church(church_id=church_id)
        return Response(
            {
                "message": "Church deactivated successfully.",
                "data": CreateChurchSerializer(church).data,
            },
            status=status.HTTP_200_OK,
        )


class NumberOfChurchesAPI(APIView):
    def get(self, request):
        total_churches = ChurchService.get_total_churches()
        return Response(
            {
                "message": "Total number of churches retrieved successfully.",
                "total": total_churches,
            },
            status=status.HTTP_200_OK,
        )


class GetListOfActiveChurchesAPI(APIView):
    def get(self, request):
        active_churches = ChurchService.get_list_of_active_churches()
        serializer = CreateChurchSerializer(active_churches, many=True)
        return Response(
            {
                "message": "Active churches retrieved successfully.",
                "total": active_churches.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class GetListOfInactiveChurchesAPI(APIView):
    def get(self, request):
        inactive_churches = ChurchService.get_list_of_inactive_churches()
        serializer = CreateChurchSerializer(inactive_churches, many=True)
        return Response(
            {
                "message": "Inactive churches retrieved successfully.",
                "total": inactive_churches.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class GetChurchByBranchIdAPI(APIView):
    def get(self, request):
        branch_id = request.query_params.get("branch_id")
        if not branch_id:
            return Response(
                {"message": "branch_id query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        churches = ChurchService.get_church_by_branch_id(branch_id=branch_id)
        serializer = CreateChurchSerializer(churches, many=True)
        return Response(
            {
                "message": "Churches retrieved successfully.",
                "total": churches.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class SearchChurchesByCityAPI(APIView):
    def get(self, request):
        city = request.query_params.get("city")
        if not city:
            return Response(
                {"message": "city query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        church = ChurchService.get_church_by_city(city=city)
        serializer = CreateChurchSerializer(church, many=True)
        return Response(
            {
                "message": "Church retrieved successfully.",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class SearchChurchesAPI(APIView):

    def get(self, request):
        churches = Church.objects.all()

        city = request.query_params.get("city")
        branch = request.query_params.get("branch")
        name = request.query_params.get("name")
        code = request.query_params.get("code")
        pastor = request.query_params.get("pastor_name")

        if city:
            churches = churches.filter(city__icontains=city)

        if branch:
            churches = churches.filter(branch_id=branch)

        if name:
            churches = churches.filter(name__icontains=name)

        if code:
            churches = churches.filter(code__icontains=code)

        if pastor:
            churches = churches.filter(pastor_name__icontains=pastor)

        serializer = CreateChurchSerializer(churches, many=True)

        return Response(serializer.data)


class GetAllChurchesNamesByCityAPI(APIView):
    def get(self, request):
        city = request.query_params.get("city")
        if not city:
            return Response(
                {"message": "city query parameter is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        churches = ChurchService.get_churches_names_by_city(city=city)
        return Response(
            {
                "message": "Church names retrieved successfully.",
                "data": churches,
            },
            status=status.HTTP_200_OK,
        )
