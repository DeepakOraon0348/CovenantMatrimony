from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .services import BranchService
from rest_framework.permissions import IsAuthenticated

class CreateBranchAPI(APIView):
    
    def post(self, request):

        serializer = CreateBranchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        branch = BranchService.create_branch(serializer.validated_data)

        return Response(
            {
                "message": "Branch created successfully.",
                "data": CreateBranchSerializer(branch).data,
            },
            status=status.HTTP_201_CREATED,
        )


class UpdateBranchAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id):
        serializer = CreateBranchSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        branch = BranchService.update_branch(
            branch_id=id,
            validated_data=serializer.validated_data,
        )

        return Response(
            {
                "message": "Branch updated successfully.",
                "data": CreateBranchSerializer(branch).data,
            },
            status=status.HTTP_200_OK,
        )


class GetAllBranchAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):

        branches = BranchService.get_all_branches()

        serializer = CreateBranchSerializer(branches, many=True)

        return Response(
            {
                "message": "Branches fetched successfully.",
                "count": len(serializer.data),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class DeleteBranchAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        branch_id = request.query_params.get("id")
        deletebranch = BranchService.Delete_branch(branch_id=branch_id)

        return Response(
            {"message": "Branch Deleted successfully.", "status": deletebranch},
            status=status.HTTP_200_OK,
        )


class ApproveBranchAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        branch_id = request.query_params.get("id")
        approvebranch = BranchService.Approve_Branch(branch_id=branch_id)

        return Response(
            {
                "message": "Branch Approved Successfully.",
                "data": CreateBranchSerializer(approvebranch).data,
            },
            status=status.HTTP_200_OK,
        )


class GetCityBranchAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        city = request.query_params.get("city")
        allcitybranch = BranchService.get_city_branch(city=city)

        return Response(
            {
                "message": "all branches",
                "data": CreateBranchSerializer(allcitybranch).data,
            },
            status=status.HTTP_200_OK,
        )


class RejectBranchAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        branch_id = request.query_params.get("Branch_id")

        rejectBranch = BranchService.Reject_Branch(branch_id=branch_id)

        return Response(
            {
                "message": "This Branch Rejected.",
                "data": CreateBranchSerializer(rejectBranch).data,
            },
            status=status.HTTP_200_OK,
        )


class ActivateBranchAPI(APIView):
    def post(self, request):
        branch_id = request.query_params.get("Branch_id")
        activateBranch = BranchService.Activate_Branch(branch_id=branch_id)

        return Response(
            {
                "message": "brach is Activated",
                "data": CreateBranchSerializer(activateBranch).data,
            },
            status=status.HTTP_200_OK,
        )


class DeactivateBranchAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        branch_id = request.query_params.get("Branch_id")
        deactivateBranch = BranchService.Deactivate_Branch(branch_id=branch_id)

        return Response(
            {
                "message": "Branch is Deactived",
                "data": CreateBranchSerializer(deactivateBranch).data,
            },
            status=status.HTTP_200_OK,
        )


class NumberOfBranch(APIView):
    def get(self, request):

        branches = BranchService.Count_Branch()
        # serializers = CreateBranchSerializer(branches, many=True)

        return Response(
            {
                "message": "Number total branchs",
                "count": branches,
            },
            status=status.HTTP_200_OK,
        )


class TotalApprovedBranch(APIView):
    def get(self, request):
        approvedBranchs = BranchService.Approved_Branch()

        return Response(
            {
                "message": "Numbers of Approved Branch",
                "total": approvedBranchs,
            },
            status=status.HTTP_200_OK,
        )


class ListOfApprovedBranchesAPI(APIView):
    def get(self, request):
        approvedBranches = BranchService.Approved_Branches()
        serializer = CreateBranchSerializer(approvedBranches, many=True)

        return Response(
            {
                "message": "List of Approved Branch",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class NumbersOfPendingAPI(APIView):
    def get(self, request):
        NumberOfPending = BranchService.Pending_Branches()

        return Response(
            {
                "message": "Total num of Pending Branches.",
                "data": NumberOfPending,
            },
            status=status.HTTP_200_OK,
        )


class ListOfPendingBranchAPI(APIView):
    def get(self, request):
        allPendingBranch = BranchService.List_Of_Pendign_branch()

        serializer = CreateBranchSerializer(allPendingBranch, many=True)

        return Response(
            {
                "message": "List of Pending Branch",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


class RejectedBranchesAPI(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        rejectedBranch = BranchService.Rejected_Branch()

        serializer = CreateBranchSerializer(rejectedBranch, many=True)

        return Response(
            {
                "message": "All Rejected list.",
                "total": len(serializer.data),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
    