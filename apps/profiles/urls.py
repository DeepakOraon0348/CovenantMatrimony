from django.urls import path
from . import views

urlpatterns = [
    path("CreateProfile/", views.CreateProfileAPI.as_view(), name="create-profile"),
    path(
        "updateProfile/<int:profile_id>/",
        views.UpdateProfileAPI.as_view(),
        name="update_profile",
    ),
    path(
        "deleteProfile/",
        views.DeleteProfileAPI.as_view(),
        name="delete_profile",
    ),
    path(
        "getMyProfile/",
        views.GetMyProfileAPI.as_view(),
        name="get_my_profile",
    ),
    path(
        "GetProfileById/", views.GetProfileByIdAPI.as_view(), name="get-profile-by-id"
    ),
    path("GetAllProfile/", views.GetAllProfileAPI.as_view(), name="get-all-profile"),
    path(
        "GetActiveProfile/",
        views.GetActiveProfileAPI.as_view(),
        name="get-active-profile",
    ),
    path(
        "GetInActiveProfile/",
        views.GetInActiveProfileAPI.as_view(),
        name="get-in-active-profile",
    ),
    path(
        "MakeInactiveProfile/",
        views.MakeInactiveProfileAPI.as_view(),
        name="make-inactive-profile",
    ),
    path("VerifyProfile/", views.VerifyProfileAPI.as_view(), name="Verify-Profile"),
    path(
        "GetAllVerifiedProfile/",
        views.GetAllVerifiedProfile.as_view(),
        name="get-all-verified-profile",
    ),
    path(
        "VerifiedPhotoVisiblity/",
        views.VerifiedPhotoVisiblityAPI.as_view(),
        name="verified-Photo-Visiblity",
    ),
    path(
        "searchProfiles/",
        views.SearchProfilesAPI.as_view(),
        name="search_profiles",
    ),
    path(
        "UpdatePhoto/<int:profile_id>/",
        views.UpdateProfilePhotoAPI.as_view(),
        name="Update-Photo",
    ),
    path(
        "ProfileApproval/", views.ProfileApprovalAPI.as_view(), name="Profile-Approval"
    ),
    path(
        "RejectProfile/",
        views.RejectProfileAPI.as_view(),
        name="reject-profile",
    ),
]
