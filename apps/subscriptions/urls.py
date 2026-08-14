
from django.urls import path

from . import views


urlpatterns = [

    path("CreatePlan/",views.CreateSubscriptionPlanAPI.as_view(),name="CreateSubscriptionPlan"),
    path("GetAllPlans/",views.GetAllSubscriptionPlansAPI.as_view(),name="GetAllSubscriptionPlans"),
    path("GetPlan/",views.GetSubscriptionPlanAPI.as_view(),name="GetSubscriptionPlan"),
    path("UpdatePlan/<int:plane_id>/",views.UpdateSubscriptionPlanAPI.as_view(),name="UpdateSubscriptionPlan"),
    path("DeletePlan/",views.DeleteSubscriptionPlanAPI.as_view(),name="DeleteSubscriptionPlan"),
]

