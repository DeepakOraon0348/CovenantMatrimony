from django.shortcuts import get_object_or_404

from apps.profiles.models import Profile
from .models import Document, DocumentStatus


class DocumentService:

    @staticmethod
    def upload_documents(profile_id, validated_data):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
        )

        document, created = Document.objects.get_or_create(
            profile=profile
        )

        for field, value in validated_data.items():

         setattr(document, field, value)

         status_field = f"{field}_status"

        if hasattr(document, status_field):
         setattr(
            document,
            status_field,
            DocumentStatus.PENDING,
        )

        document.save()

        return document

    @staticmethod
    def get_my_documents(profile_id, user):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
            user=user,
        )

        return get_object_or_404(
            Document,
            profile=profile,
        )
    @staticmethod 
    def admin_get_documents(profile_id):
        document=Document.objects.filter(profile=profile_id).first();
        return document;   

    @staticmethod
    def update_documents(profile_id, user, validated_data):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
            user=user,
        )

        document = get_object_or_404(
            Document,
            profile=profile,
        )

        for field, value in validated_data.items():

            setattr(document, field, value)

            status_field = f"{field}_status"

            if hasattr(document, status_field):
                setattr(
                    document,
                    status_field,
                    DocumentStatus.PENDING,
                )

        document.save()

        return document
    
    @staticmethod
    def aadhar_approve(profile_id):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
        )

        document = get_object_or_404(
            Document,
            profile=profile,
        )

        if not document.aadhaar:
            raise ValueError(
                "Aadhaar document has not been uploaded."
            )

        document.aadhaar_status = DocumentStatus.APPROVED

        document.save(
            update_fields=[
                "aadhaar_status",
                "updated_at",
            ]
        )

        return document

    @staticmethod
    def delete_document(profile_id, user, document_field):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
            user=user,
        )

        document = get_object_or_404(
            Document,
            profile=profile,
        )

        if not hasattr(document, document_field):
            raise ValueError("Invalid document field.")

        setattr(document, document_field, None)

        status_field = f"{document_field}_status"

        if hasattr(document, status_field):
            setattr(
                document,
                status_field,
                DocumentStatus.PENDING,
            )

        document.save()

        return document
    
    
    @staticmethod
    def reject_Aadhar(profile_id):
        profile = get_object_or_404(
                    Profile,
                    id=profile_id,
                )
        
        document = get_object_or_404(
                    Document,
                    profile=profile,
                )
        
        if not document.aadhaar:
                    raise ValueError(
                        "Aadhaar document has not been uploaded."
                    )
        
        document.aadhaar_status = DocumentStatus.REJECTED
        
        document.save(
                    update_fields=[
                        "aadhaar_status",
                        "updated_at",
                    ]
                )
        
        return document
    
    @staticmethod
    def approve_baptism(profile_id):

      profile = get_object_or_404(
        Profile,
        id=profile_id,
      )

      document = get_object_or_404(
        Document,
        profile=profile,
      )

      if not document.baptism_certificate:
        raise ValueError(
            "Baptism certificate has not been uploaded."
        )

      document.baptism_certificate_status = DocumentStatus.APPROVED

      document.save(
        update_fields=[
            "baptism_certificate_status",
            "updated_at",
        ]
      )

      return document
  
    @staticmethod
    def reject_baptism(profile_id):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
        )

        document = get_object_or_404(
            Document,
            profile=profile,
        )

        if not document.baptism_certificate:
            raise ValueError(
                "Baptism certificate has not been uploaded."
            )

        document.baptism_certificate_status = DocumentStatus.REJECTED

        document.save(
            update_fields=[
                "baptism_certificate_status",
                "updated_at",
            ]
        )

        return document
    
    @staticmethod
    def approve_education(profile_id):

       profile = get_object_or_404(
            Profile,
            id=profile_id,
       )

       document = get_object_or_404(
            Document,
            profile=profile,
        )

       if not document.education_certificate:
            raise ValueError(
                "Education certificate has not been uploaded."
            )

       document.education_certificate_status = DocumentStatus.APPROVED

       document.save(
            update_fields=[
                "education_certificate_status",
                "updated_at",
           ]
        )

       return document
   
    @staticmethod
    def reject_education(profile_id):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
        )

        document = get_object_or_404(
            Document,
            profile=profile,
        )

        if not document.education_certificate:
            raise ValueError(
                "Education certificate has not been uploaded."
            )

        document.education_certificate_status = DocumentStatus.REJECTED

        document.save(
            update_fields=[
                "education_certificate_status",
                "updated_at",
            ]
        )

        return document
    
    @staticmethod
    def approve_income(profile_id):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
        )

        document = get_object_or_404(
            Document,
            profile=profile,
        )

        if not document.income_certificate:
            raise ValueError(
                "Income certificate has not been uploaded."
            )

        document.income_certificate_status = DocumentStatus.APPROVED

        document.save(
            update_fields=[
                "income_certificate_status",
                "updated_at",
            ]
        )

        return document
    
    @staticmethod
    def reject_income(profile_id):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
        )

        document = get_object_or_404(
            Document,
            profile=profile,
        )

        if not document.income_certificate:
            raise ValueError(
                "Income certificate has not been uploaded."
            )

        document.income_certificate_status = DocumentStatus.REJECTED

        document.save(
            update_fields=[
                "income_certificate_status",
                "updated_at",
            ]
        )

        return document
    
    @staticmethod
    def approve_other_document(profile_id):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
        )

        document = get_object_or_404(
            Document,
            profile=profile,
        )

        if not document.other_document:
            raise ValueError(
                "Other document has not been uploaded."
            )

        document.other_document_status = DocumentStatus.APPROVED

        document.save(
            update_fields=[
                "other_document_status",
                "updated_at",
            ]
        )

        return document
    
    @staticmethod
    def reject_other_document(profile_id):

        profile = get_object_or_404(
            Profile,
            id=profile_id,
        )

        document = get_object_or_404(
            Document,
            profile=profile,
        )

        if not document.other_document:
            raise ValueError(
                "Other document has not been uploaded."
            )

        document.other_document_status = DocumentStatus.REJECTED

        document.save(
            update_fields=[
                "other_document_status",
                "updated_at",
            ]
        )

        return document