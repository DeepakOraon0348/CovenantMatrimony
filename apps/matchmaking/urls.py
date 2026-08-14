from django.urls import path

from . import views


urlpatterns = [

    # =========================================
    # INTEREST REQUEST
    # =========================================

    path(
        "CreateInterest/",
        views.CreateInterestRequestAPI.as_view(),
        name="create-interest",
    ),

    path(
        "GetSentInterest/",
        views.GetSentInterestRequestsAPI.as_view(),
        name="get-sent-interest",
    ),

    path(
        "GetReceivedInterest/",
        views.GetReceivedInterestRequestsAPI.as_view(),
        name="get-received-interest",
    ),

    path(
        "GetInterest/",
        views.GetInterestRequestAPI.as_view(),
        name="get-interest",
    ),

    path(
        "AcceptInterest/",
        views.AcceptInterestRequestAPI.as_view(),
        name="accept-interest",
    ),

    path(
        "RejectInterest/",
        views.RejectInterestRequestAPI.as_view(),
        name="reject-interest",
    ),

    path(
        "CancelInterest/",
        views.CancelInterestRequestAPI.as_view(),
        name="cancel-interest",
    ),

    # =========================================
    # MATCH
    # =========================================

    path(
        "GetMyMatches/",
        views.GetMyMatchesAPI.as_view(),
        name="get-my-matches",
    ),

    path(
        "GetMatch/",
        views.GetMatchAPI.as_view(),
        name="get-match",
    ),

    path(
        "CloseMatch/",
        views.CloseMatchAPI.as_view(),
        name="close-match",
    ),
]