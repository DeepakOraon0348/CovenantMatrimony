from django.urls import path

from . import views


urlpatterns = [

    path("CreatePrayer/", views.CreatePrayerAPI.as_view(), name="create-prayer"),

    path("GetAllPrayer/", views.GetAllPrayerAPI.as_view(), name="get-all-prayer"),

    path("GetMyChurchPrayer/", views.GetMyChurchPrayerAPI.as_view(), name="get-my-church-prayer"),

    path("GetPrayer/", views.GetPrayerAPI.as_view(), name="get-prayer"),

    path("UpdatePrayer/", views.UpdatePrayerAPI.as_view(), name="update-prayer"),

    path("UpdatePrayerStatus/", views.UpdatePrayerStatusAPI.as_view(), name="update-prayer-status"),

    path("DeletePrayer/", views.DeletePrayerAPI.as_view(), name="delete-prayer"),

]