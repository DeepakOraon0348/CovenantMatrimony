from django.templatetags import static
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("createChurch/", views.CreateChurchAPI.as_view(), name="create_church"),
    path(
        "updateChurch/<int:church_id>/",
        views.UpdateChurchAPI.as_view(),
        name="update_church",
    ),
    path(
        "getAllChurches/",
        views.GetAllChurchesAPI.as_view(),
        name="get_all_churches",
    ),
    path(
        "getChurchById/",
        views.GetChurchByIdAPI.as_view(),
        name="get_church_by_id",
    ),
    path("deleteChurch/", views.DeleteChurchAPI.as_view(), name="delete_church"),
    path("approveChurch/", views.ApproveChurchAPI.as_view(), name="approve_church"),
    path("rejectChurch/", views.RejectChurchAPI.as_view(), name="reject_church"),
    path(
        "getApprovedChurches/",
        views.GetApprovedChurchesAPI.as_view(),
        name="get_approved_churches",
    ),
    path(
        "getAllRejectedChurches/",
        views.GetAllRejectedChurchesAPI.as_view(),
        name="get_rejected_churches",
    ),
    path(
        "getAllPendingChurches/",
        views.GetAllPendingChurchesAPI.as_view(),
        name="get_pending_churches",
    ),
    path(
        "activateChurch/",
        views.ActivateChurchAPI.as_view(),
        name="activate_church",
    ),
    path(
        "deactivateChurch/",
        views.DeactivateChurchAPI.as_view(),
        name="deactivate_church",
    ),
    path(
        "numberOfChurches/",
        views.NumberOfChurchesAPI.as_view(),
        name="number_of_churches",
    ),
    path(
        "getListOfActiveChurches/",
        views.GetListOfActiveChurchesAPI.as_view(),
        name="get_list_of_active_churches",
    ),
    path(
        "getListOfInactiveChurches/",
        views.GetListOfInactiveChurchesAPI.as_view(),
        name="get_list_of_inactive_churches",
    ),
    path(
        "getChurchByBranchId/",
        views.GetChurchByBranchIdAPI.as_view(),
        name="get_church_by_branch_id",
    ),
    path(
        "searchChurchesbyCity/",
        views.SearchChurchesByCityAPI.as_view(),
        name="search_churches",
    ),
    path(
        "searchChurches/",
        views.SearchChurchesAPI.as_view(),
        name="search_churches",
    ),
    path(
        "getAllChurchesNamesByCity/",
        views.GetAllChurchesNamesByCityAPI.as_view(),
        name="get_all_churches_names_by_city",
    ),
]

