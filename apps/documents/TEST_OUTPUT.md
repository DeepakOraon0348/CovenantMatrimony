# 1. Uploade documents API: http://127.0.0.1:8000/api/documents/UploadDocuments/4/
## Methods: Post
## Query parameters: form-data

- Request:-
```json
{
    "aadhaar":
    "baptism_certificate":
    "education_certificate"
    "income_certificate"
    "profile_id":,
    "other_document":,
}
```
- Response:-
```json
{
    "message": "Documents uploaded successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/agami_technology-msg.png",
        "baptism_certificate": "/profiles/documents/baptism/AI_voice_Assistant.png",
        "education_certificate": "/profiles/documents/education/agami_technology-msg.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant.png",
        "other_document": null,
        "aadhaar_status": "PENDING",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T07:19:13.229641Z",
        "profile": 4
    }
}
```
# 2. Update Documents API: http://127.0.0.1:8000/api/documents/UpdateDocuments/4/
## Methods: PUT,
## Query-Parameters:form-data
- Request:-
```json
{
     "aadhaar":
    "baptism_certificate":
    "education_certificate"
    "income_certificate"
    "profile_id":4,
}
```
- Response:-
```json
{
    "message": "Documents updated successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_mQZnzQQ.png",
        "other_document": null,
        "aadhaar_status": "PENDING",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T07:30:15.816485Z",
        "profile": 4
    }
}
```

# 3. Fetch documents by id API: http://127.0.0.1:8000/api/documents/GetMyDocuments/?profile_id=4
## Method: get
## Query-Parameters: no
- Response:- 
```json
{
    "message": "Documents fetched successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_mQZnzQQ.png",
        "other_document": null,
        "aadhaar_status": "PENDING",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T07:30:15.816485Z",
        "profile": 4
    }
}
```
# 4. Aadhar Approval API: http://127.0.0.1:8000/api/documents/ApproveAadhar/?profile_id=4
## Methods: PATCH
## Query-Parameters: params
- Request:-
```json
{
    "profile_id":4,
}
```
- Response:-
```json
{
    "message": "Aadhaar approved successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_mQZnzQQ.png",
        "other_document": null,
        "aadhaar_status": "APPROVED",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T07:55:26.319294Z",
        "profile": 4
    }
}
```
# 5. Aadhar Rejection API: http://127.0.0.1:8000/api/documents/RejectAadhar/?profile_id=4
## Method: PATCH
## Query-Parameters: params
- Request:-
```json
{
    "profile_id":4,
}
```
- Response:-
```json
{
    "message": "Aadhar Rejected Successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_mQZnzQQ.png",
        "other_document": null,
        "aadhaar_status": "REJECTED",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T08:20:47.346520Z",
        "profile": 4
    }
}
```

# 6. Baptims approved API: http://127.0.0.1:8000/api/documents/ApproveBaptism/?profile_id=4
## Method: PATCH
## Query Parameters: params
- Request:-
```json
{
    "profile_id":4,
}
```
- Respose:-
```json
{
    "message": "Baptism approved successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_mQZnzQQ.png",
        "other_document": null,
        "aadhaar_status": "REJECTED",
        "baptism_certificate_status": "APPROVED",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T09:16:07.022018Z",
        "profile": 4
    }
}
```
# 7. Baptism Rejecting API: http://127.0.0.1:8000/api/documents/RejectBaptism/?profile_id=4
## Method: PATCH
## Query-parameters: params
- Request:-
```json
{
    "profile_id":4,
}
```
- Response:-
```json
{
    "message": "Baptism Reject Successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_mQZnzQQ.png",
        "other_document": null,
        "aadhaar_status": "REJECTED",
        "baptism_certificate_status": "REJECTED",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T09:35:33.086161Z",
        "profile": 4
    }
}
```
# 8. Approve Eduction Certificate API: http://127.0.0.1:8000/api/documents/ApproveEducationCertificate/?profile_id=4
## Methods: patch
## Query Parameters: params
- Request:-
```json
{
    "profile_id":4,
}
```
- Response:-
```json
{
    "message": "Approve education certificate successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_mQZnzQQ.png",
        "other_document": null,
        "aadhaar_status": "REJECTED",
        "baptism_certificate_status": "REJECTED",
        "education_certificate_status": "APPROVED",
        "income_certificate_status": "PENDING",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T10:10:19.629073Z",
        "profile": 4
    }
}
```

# 9. Reject Education Certificate API:  http://127.0.0.1:8000/api/documents/RejectEducationCertificate/?profile_id=4
## Method: PATCH
## Query Parameters: params
- Request:-
```json
{
    "profile-id":4,
}
```
- Response:-
```json
{
    "message": "Education certificate Rejected successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_mQZnzQQ.png",
        "other_document": null,
        "aadhaar_status": "REJECTED",
        "baptism_certificate_status": "REJECTED",
        "education_certificate_status": "REJECTED",
        "income_certificate_status": "PENDING",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T10:40:46.830291Z",
        "profile": 4
    }
}
```

# 10. Approve Income certificate API: http://127.0.0.1:8000/api/documents/ApproveIncomeCertificate/?profile_id=4
## Methods: PATCH
## Query parameters: params
- Request:-
```json
{
    "profile_id":4,
}
```
- Response:-
```json
{
    "message": "Income certificate approved successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_mQZnzQQ.png",
        "other_document": null,
        "aadhaar_status": "REJECTED",
        "baptism_certificate_status": "REJECTED",
        "education_certificate_status": "REJECTED",
        "income_certificate_status": "APPROVED",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T11:18:29.427602Z",
        "profile": 4
    }
}
```

# 11. Reject income certificate API: http://127.0.0.1:8000/api/documents/RejectIncomeCertificate/?profile_id=4
## Method: Patch
## Query Parameters: profile_id

- Request:-
```json
{
    "profile_id":4,
}
```
- Response:-
```json
{
    "message": "Income certificate rejected successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_mQZnzQQ.png",
        "other_document": null,
        "aadhaar_status": "REJECTED",
        "baptism_certificate_status": "REJECTED",
        "education_certificate_status": "REJECTED",
        "income_certificate_status": "REJECTED",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T11:40:48.085885Z",
        "profile": 4
    }
}
```
# 12. Approve other documents API: http://127.0.0.1:8000/api/documents/ApproveOtherDocument/?profile_id=4
## Method: Patch
## query parameters: params

- Request:-
```json
{
    "profile_id":4,
}
```

- Response:-
```json
{
    "message": "Other documents approve successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant_t7pF0Qp.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg_YzBNehy.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant_JGofMru.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_orqb83N.png",
        "other_document": "/profiles/documents/other/AI_voice_Assistant.png",
        "aadhaar_status": "PENDING",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "APPROVED",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T12:05:53.128353Z",
        "profile": 4
    }
}
```
# 13. Reject other ducuments API: http://127.0.0.1:8000/api/documents/RejectOtherDocument/?profile_id=4
## Method: patch
## Query Parameters: params
- Request:-
```json
{
    "profile_id":4,
}
```
- Response:-
```json
{
    "message": "Other documents rejected successfully.",
    "data": {
        "id": 1,
        "aadhaar": "/profiles/documents/aadhaar/AI_voice_Assistant_t7pF0Qp.png",
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg_YzBNehy.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant_JGofMru.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_orqb83N.png",
        "other_document": "/profiles/documents/other/AI_voice_Assistant.png",
        "aadhaar_status": "PENDING",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "REJECTED",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-10T12:30:07.223014Z",
        "profile": 4
    }
}
```
# 14. Delete aadhaar API: http://127.0.0.1:8000/api/documents/DeleteDocument/4/
## Method: DELETE
## Query Parameters: form-data,
- profile_id pass in URL parameters

- Request:-
```json
{
    "document_field":"aadhaar",
}
```

- Response:-
```json
{
    "message": "Document deleted successfully.",
    "data": {
        "id": 1,
        "aadhaar": null,
        "baptism_certificate": "/profiles/documents/baptism/agami_technology-msg_YzBNehy.png",
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant_JGofMru.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_orqb83N.png",
        "other_document": "/profiles/documents/other/AI_voice_Assistant.png",
        "aadhaar_status": "PENDING",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "REJECTED",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-11T05:02:03.961409Z",
        "profile": 4
    }
}
```

# 15.Delete baptism certificate API: http://127.0.0.1:8000/api/documents/DeleteDocument/4/
## Method: DELETE
## Query parameters:-form-data
- profile_id pass thourgh an URL parameters.
- Request:-
```json
{

    "document_field":"baptism_certificate",
}
```
- Request:-
```json
{
    "message": "Document deleted successfully.",
    "data": {
        "id": 1,
        "aadhaar": null,
        "baptism_certificate": null,
        "education_certificate": "/profiles/documents/education/AI_voice_Assistant_JGofMru.png",
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_orqb83N.png",
        "other_document": "/profiles/documents/other/AI_voice_Assistant.png",
        "aadhaar_status": "PENDING",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "REJECTED",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-11T05:08:55.866411Z",
        "profile": 4
    }
}
```
# 16. Delete Education Certificate API: http://127.0.0.1:8000/api/documents/DeleteDocument/4/
## Methods: DELETE
## Query Parameters: form-data
- profile_id pass through an URL parameters.
- Request:-
```json
{
    "document_field":"education_certificate",
}
```

- Response:-
```json
{
    "message": "Document deleted successfully.",
    "data": {
        "id": 1,
        "aadhaar": null,
        "baptism_certificate": null,
        "education_certificate": null,
        "income_certificate": "/profiles/documents/income/AI_voice_Assistant_orqb83N.png",
        "other_document": "/profiles/documents/other/AI_voice_Assistant.png",
        "aadhaar_status": "PENDING",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "REJECTED",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-11T05:13:31.364112Z",
        "profile": 4
    }
}
```

# 17. Delete income certificate API: http://127.0.0.1:8000/api/documents/DeleteDocument/4/
## Method: DELETE
## Query parameters: form-data
- profile_id pass through an URL parameters
- Request:-
```json
{
    "document_field":"income_certificate",
}

```
- Response:-
```json
{
    "message": "Document deleted successfully.",
    "data": {
        "id": 1,
        "aadhaar": null,
        "baptism_certificate": null,
        "education_certificate": null,
        "income_certificate": null,
        "other_document": "/profiles/documents/other/AI_voice_Assistant.png",
        "aadhaar_status": "PENDING",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "REJECTED",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-11T05:21:13.956373Z",
        "profile": 4
    }
}
```
# 18. Delete other documents API:http://127.0.0.1:8000/api/documents/DeleteDocument/4/
## Method: DELETE
## Query Parameters: form-data
- profile_id pass through an URL parameters
- Request
```json
{
    "document_field":"other_document"
}
```

- Response:- 
```json
{
    "message": "Document deleted successfully.",
    "data": {
        "id": 1,
        "aadhaar": null,
        "baptism_certificate": null,
        "education_certificate": null,
        "income_certificate": null,
        "other_document": null,
        "aadhaar_status": "PENDING",
        "baptism_certificate_status": "PENDING",
        "education_certificate_status": "PENDING",
        "income_certificate_status": "PENDING",
        "other_document_status": "PENDING",
        "created_at": "2026-08-10T07:19:13.200976Z",
        "updated_at": "2026-08-11T05:24:02.641768Z",
        "profile": 4
    }
}
```