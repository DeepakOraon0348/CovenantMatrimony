from django.urls import path
from . import views

urlpatterns = [
    path(
        "CreateDenomination/",
        views.CreateDenominationAPI.as_view(),
        name="Create-Denomination",
    ),
    path(
        "GetAllDenomination/",
        views.GetAllDenominationAPI.as_view(),
        name="get-all-denomination",
    ),
]
