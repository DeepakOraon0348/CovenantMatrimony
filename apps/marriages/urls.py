from django.urls import path

from . import views


urlpatterns = [

    path("CreateMarriage/", views.CreateMarriageAPI.as_view(), name="create-marriage"),

    path("GetAllMarriage/", views.GetAllMarriageAPI.as_view(), name="get-all-marriage"),

    path("GetMyMarriage/", views.GetMyMarriageAPI.as_view(), name="get-my-marriage"),

    path("GetMarriage/", views.GetMarriageAPI.as_view(), name="get-marriage"),

    path("UpdateMarriage/<int:marriage_id>/", views.UpdateMarriageAPI.as_view(), name="update-marriage"),

    path("UpdateMarriageStatus/", views.UpdateMarriageStatusAPI.as_view(), name="update-marriage-status"),

    path("DeleteMarriage/<int:marriage_id>/", views.DeleteMarriageAPI.as_view(), name="delete-marriage"),
]