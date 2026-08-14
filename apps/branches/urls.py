from django.urls import path
from .views import *

urlpatterns = [
    path("CreateBranch/", CreateBranchAPI.as_view(), name="CreateBranch"),
    path("UpdateBranch/<int:id>/", UpdateBranchAPI.as_view(), name="UpdateBranch"),
    path("GetAllBranch/", GetAllBranchAPI.as_view(), name="GetAllBranch"),
    path("DeleteBranch/", DeleteBranchAPI.as_view(), name="DeleteBranch"),
    path("ApproveBranch/", ApproveBranchAPI.as_view(), name="ApproveBranch"),
    path("RejectBranch/", RejectBranchAPI.as_view(), name="RejectBranch"),
    path("GetCityBranch/", GetCityBranchAPI.as_view(), name="GetCityBranch"),
    path("ActivateBranch/", ActivateBranchAPI.as_view(), name="ActivateBranch"),
    path("DeactivateBranch/", DeactivateBranchAPI.as_view(), name="DeactivateBranch"),
    path("NumberOfBranch/", NumberOfBranch.as_view(), name="NumberOfBranch"),
    path(
        "TotalApprovedBranch/",
        TotalApprovedBranch.as_view(),
        name="TotalApprovedBranch",
    ),
    path(
        "ListOfApprovedBranches/",
        ListOfApprovedBranchesAPI.as_view(),
        name="ListOfApprovedBranches",
    ),
    path("NumbersOfPending/", NumbersOfPendingAPI.as_view(), name="NumbersOfPending"),
    path(
        "ListOfPendingBranch/",
        ListOfPendingBranchAPI.as_view(),
        name="ListOfPendingBranch",
    ),
    path("RejectedBranches/", RejectedBranchesAPI.as_view(), name="RejectedBranches"),
]
