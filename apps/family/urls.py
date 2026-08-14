from django.urls import path

from . import views


urlpatterns = [

    path(
        "CreateFamily/<int:profile_id>/",
        views.CreateFamilyAPI.as_view(),
        name="create-family",
    ),

    path(
        "GetMyFamily/",
        views.GetMyFamilyAPI.as_view(),
        name="get-my-family",
    ),

    path(
        "UpdateFamily/<int:profile_id>/",
        views.UpdateFamilyAPI.as_view(),
        name="update-family",
    ),

    path(
        "DeleteFamily/",
        views.DeleteFamilyAPI.as_view(),
        name="delete-family",
    ),
]