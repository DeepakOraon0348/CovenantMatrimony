from django.urls import path
from . import views

urlpatterns = [
    path("CreateAccount/", views.CreateAccountAPI.as_view(), name="Create-Account"),
    path("UserLogin/", views.UserLoginAPI.as_view(), name="user-login"),
    path("GetAllRegisterUser/", views.GetAllRegisterUser.as_view(), name="get-all-register-user"),
    path("NumbersOfRegisterUser/", views.NumbersOfRegisterUserAPI.as_view(), name="numbers-of-register-user"),
    path("MyDashboard/", views.MyDashboardAPI.as_view(), name="my-dashboard"),
]
