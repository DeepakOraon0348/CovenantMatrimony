from django.urls import path

from . import views


urlpatterns = [

    path("CreateSubscription/", views.CreateUserSubscriptionAPI.as_view(), name="create-subscription"),
    path("GetMySubscription/", views.GetMySubscriptionAPI.as_view(), name="get-my-subscription"),
    path("GetSubscriptionById/", views.GetUserSubscriptionByIdAPI.as_view(), name="get-subscription-by-id"),
    path("CancelSubscription/", views.CancelUserSubscriptionAPI.as_view(), name="cancel-subscription"),
]