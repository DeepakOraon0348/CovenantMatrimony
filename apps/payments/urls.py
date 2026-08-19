from django.urls import path

from . import views


urlpatterns = [

    path("CreatePayment/", views.CreatePaymentAPI.as_view(), name="create-payment"),

    path("VerifyPayment/", views.VerifyPaymentAPI.as_view(), name="verify-payment"),

    path("GetMyPayments/", views.GetMyPaymentsAPI.as_view(), name="get-my-payments"),

    path("GetPayment/", views.GetPaymentAPI.as_view(), name="get-payment"),
    path("AdminVerifyPayment/", views.AdminVerifyPaymentAPI.as_view(), name="admin-verify-payment"),

]