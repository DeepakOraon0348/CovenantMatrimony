from django.urls import path

from . import views


urlpatterns = [

   path(
    "UploadDocuments/<int:profile_id>/",
    views.UploadDocumentsAPI.as_view(),
    name="upload-documents",
),

    path(
        "UpdateDocuments/<int:profile_id>/",
        views.UpdateDocumentsAPI.as_view(),
        name="update-documents",
    ),

    path(
        "GetMyDocuments/",
        views.GetMyDocumentsAPI.as_view(),
        name="get-my-documents",
    ),
    path("ApproveAadhar/", views.ApproveAadharAPI.as_view(), name="approve-aadhar"),
    path("RejectAadhar/", views.RejectAadharAPI.as_view(), name="reject-aadhar"),
    path("ApproveBaptism/", views.ApproveBaptismAPI.as_view(), name="approve-baptism"),
    path("RejectBaptism/", views.RejectBaptismAPI.as_view(), name="reject-baptism"),
    path("ApproveEducationCertificate/", views.ApproveEducationCertificateAPI.as_view(), name="approve-Education-Certificate"),
    path("RejectEducationCertificate/", views.RejectEducationCertificateAPI.as_view(), name="reject-education-certificate"),
    path("ApproveIncomeCertificate/", views.ApproveIncomeCertificateAPI.as_view(), name="approve-income-certificate"),
    path("RejectIncomeCertificate/", views.RejectIncomeCertificateAPI.as_view(), name="reject-income-certificate"),
    path("ApproveOtherDocument/", views.ApproveOtherDocumentAPI.as_view(), name="approve-other-document"),
    path("RejectOtherDocument/", views.RejectOtherDocumentAPI.as_view(), name="reject-other-document"),
    

    path(
        "DeleteDocument/<int:profile_id>/",
        views.DeleteDocumentAPI.as_view(),
        name="delete-document",
    ),
]