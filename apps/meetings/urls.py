from django.urls import path

from . import views


urlpatterns = [

    path("CreateMeeting/", views.CreateMeetingAPI.as_view(), name="create-meeting"),
    path("GetAllMeeting/",views.GetAllMeetingAPI.as_view(), name="get-all-meeting"),
    path("GetMyMeetings/", views.GetMyMeetingsAPI.as_view(), name="get-my-meetings"),
    path("GetMeeting/", views.GetMeetingAPI.as_view(), name="get-meeting"),
    path("UpdateMeeting/", views.UpdateMeetingAPI.as_view(), name="update-meeting"),
    path("MeetingComplete/", views.MeetingCompleteAPI.as_view(), name="meeting-complete"),
    path("CancelMeeting/", views.CancelMeetingAPI.as_view(), name="cancel-meeting"),

]