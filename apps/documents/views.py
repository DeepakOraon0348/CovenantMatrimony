from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import DocumentSerializer
from .services import DocumentService


class UploadDocumentsAPI(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, profile_id):

        serializer = DocumentSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        document = DocumentService.upload_documents(
            profile_id=profile_id,
            # user=request.user,
            validated_data=serializer.validated_data,
        )

        return Response(
            {
                "message": "Documents uploaded successfully.",
                "data": DocumentSerializer(document).data,
            },
            status=status.HTTP_201_CREATED,
        )


class UpdateDocumentsAPI(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, profile_id):

        serializer = DocumentSerializer(
            data=request.data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True
        )

        document = DocumentService.update_documents(
            profile_id=profile_id,
            user=request.user,
            validated_data=serializer.validated_data,
        )

        return Response(
            {
                "message": "Documents updated successfully.",
                "data": DocumentSerializer(document).data,
            },
            status=status.HTTP_200_OK,
        )


class GetMyDocumentsAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile_id=request.query_params.get("profile_id")
        if not profile_id:
            return Response(
                {
                    "message":"profile id required.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        document = DocumentService.get_my_documents(
            profile_id=profile_id,
            user=request.user,
        )

        return Response(
            {
                "message": "Documents fetched successfully.",
                "data": DocumentSerializer(document).data,
            },
            status=status.HTTP_200_OK,
        )

class AdminGetDocumentsAPI(APIView):
    parser_classes=[IsAuthenticated]

    def get(self, request):
        profile_id = request.query_params.get("profile_id")

        if not profile_id:
            return Response(
                {
                    "message": "Profile id is required.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        documents=DocumentService.admin_get_documents(profile_id=profile_id)
        if not documents:
            return Response(
                {
                    "message":"No documents found for this profile.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        print("PROFILE ID:", profile_id)
        print("DOCUMENT:", documents)

         
        serilizers=DocumentSerializer(documents);
        return Response(
            {
                "message":"User documents fetched successfully. ",
                "data":serilizers.data
            }
        )
        
class DeleteDocumentAPI(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, profile_id):

        document_field = request.data.get("document_field")

        if not document_field:
            return Response(
                {
                    "message": "Document field is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:

            document = DocumentService.delete_document(
                profile_id=profile_id,
                user=request.user,
                document_field=document_field,
            )

        except ValueError as error:

            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": "Document deleted successfully.",
                "data": DocumentSerializer(document).data,
            },
            status=status.HTTP_200_OK,
        )
        
class ApproveAadharAPI(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request):

        profile_id = request.query_params.get("profile_id")

        if not profile_id:
            return Response(
                {
                    "message": "profile_id is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            document = DocumentService.aadhar_approve(
                profile_id=profile_id,
            )

        except ValueError as error:
            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "message": "Aadhaar approved successfully.",
                "data": DocumentSerializer(document).data,
            },
            status=status.HTTP_200_OK,
        )
        
class RejectAadharAPI(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request):
        profile_id=request.query_params.get("profile_id")
        
        if not profile_id:
            return Response(
            {
                "message": "profile_id is required."
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
        try:
            reject_aadhar=DocumentService.reject_Aadhar(profile_id=profile_id)
            
        except ValueError as error:
            return Response(
                {
                    "message": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        return Response(
            {
                "message":"Aadhar Rejected Successfully.",
                "data":DocumentSerializer(reject_aadhar).data,
            },
            status=status.HTTP_200_OK,
        )
class ApproveBaptismAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request):
        profile_id=request.query_params.get("profile_id")
        
        if not profile_id:
                   return Response(
                   {
                       "message": "profile_id is required."
                   },
                   status=status.HTTP_400_BAD_REQUEST,
               )
        try:
            approved_baptism=DocumentService.approve_baptism(profile_id=profile_id)
            
        except ValueError as error:
            return Response(
            {
                "message": str(error)
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
        return Response(
            {
                "message":"Baptism approved successfully.",
                "data":DocumentSerializer(approved_baptism).data
            }
        )
class RejectBaptismAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request):
        profile_id=request.query_params.get("profile_id")
        
        if not profile_id:
            return Response(
                {
                    "message": "profile_id is required."
                },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        try: 
            reject_baptism=DocumentService.reject_baptism(profile_id=profile_id)
            
        except ValueError as error:
                    return Response(
                    {
                        "message": str(error)
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
                    
        return Response(
            {
                "message":"Baptism Reject Successfully.",
                "data":DocumentSerializer(reject_baptism).data,
            },
            status=status.HTTP_200_OK,
        )
class ApproveEducationCertificateAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request):
        profile_id=request.query_params.get("profile_id")
        
        if not profile_id:
            return Response(
                {
                    "message": "profile_id is required."
                },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        try:
            approve_education_certificate=DocumentService.approve_education(profile_id=profile_id)
            
        except ValueError as error:
            return Response(
                {
                    "message": str(error)
                },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            
        return Response(
            {
                "message":"Approve education certificate successfully.",
                "data":DocumentSerializer(approve_education_certificate).data,
            },
            status=status.HTTP_200_OK,
        )
        
class RejectEducationCertificateAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request):
        profile_id=request.query_params.get("profile_id")
        
        if not profile_id:
            return Response(
                {
                    "message":"profile id is required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        try:
            reject_education_certificate=DocumentService.reject_education(profile_id=profile_id)
            
        except ValueError as error:
            return Response(
                {
                    "message":str(error)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {
                "message":"Education certificate Rejected successfully.",
                "data":DocumentSerializer(reject_education_certificate).data,
            },
            status=status.HTTP_200_OK,
        )
        
class ApproveIncomeCertificateAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request):
        profile_id=request.query_params.get("profile_id")
        
        if not profile_id:
            return Response(
                {
                    "message":"profile id required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            approve_income=DocumentService.approve_income(profile_id)
            
        except ValueError as error:
            return Response(
                {
                    "message":str(error),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        return Response(
            {
                "message":"Income certificate approved successfully.",
                "data":DocumentSerializer(approve_income).data,
            },
            status=status.HTTP_200_OK,
        )

class RejectIncomeCertificateAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request):
        profile_id=request.query_params.get("profile_id")
        
        if not profile_id:
            return Response(
                {
                    "message":"profile id required.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            reject_income=DocumentService.reject_income(profile_id=profile_id)
        except ValueError as error:
            return Response(
                {
                    "message":str(error),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        return Response(
            {
                "message":"Income certificate rejected successfully.",
                "data":DocumentSerializer(reject_income).data,
            },
            status=status.HTTP_200_OK,
        )
class ApproveOtherDocumentAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, request):
        profile_id=request.query_params.get("profile_id")
        
        if not profile_id:
            return Response(
                {
                    "message":"profile id required.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        try: 
            approve_other_doc=DocumentService.approve_other_document(profile_id)
        except ValueError as error:
            return Response(
                {
                    "message":str(error),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
            
        return Response(
            {
                "message":"Other documents approve successfully.",
                "data":DocumentSerializer(approve_other_doc).data,
            },
            status=status.HTTP_200_OK,
        )
class RejectOtherDocumentAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def patch(self, requst):
        profile_id=self.request.query_params.get("profile_id")
        
        if not profile_id:
            return Response(
                {
                    "message":"profile id required.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            reject_other_doc=DocumentService.reject_other_document(profile_id)
        except ValueError as error:
            return Response(
                {
                    "message":str(error),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "message":"Other documents rejected successfully.",
                "data":DocumentSerializer(reject_other_doc).data,
            },
            status=status.HTTP_200_OK,
        )