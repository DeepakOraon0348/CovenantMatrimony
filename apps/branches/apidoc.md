# API for creating Branch: http://127.0.0.1:8000/api/branch/CreateBranch/
## Test Case:
## method: POST
## query parameters:from-data
```json
{
    "name": "Ranchi Branch",
    "code": "RAN001",
    "email": "ranchi.branch@example.com",
    "phone": "9876543210",
    "address": "Main Road, Lalpur",
    "city": "Ranchi",
    "state": "Jharkhand",
    "country": "India",
    "pincode": "834001",
    "description": "Regional branch serving churches across Jharkhand.",
    "verification_status": "PENDING",
    "is_active": true,
    "logo":
},
{
    "name": "Jamshedpur Branch",
    "code": "JAM001",
    "email": "jamshedpur.branch@example.com",
    "phone": "9123456789",
    "address": "Bistupur Main Road",
    "city": "Jamshedpur",
    "state": "Jharkhand",
    "country": "India",
    "pincode": "831001",
    "description": "Branch for East Singhbhum churches.",
    "verification_status": "APPROVED",
    "is_active": true
}

```
## Invalid Test Case: 
``` json
query parameters:form-data
-invalid Phone Number
{
    "name": "Test Branch",
    "code": "TES001",
    "email": "test@example.com",
    "phone": "12345",
    "address": "Test Address",
    "city": "Ranchi",
    "state": "Jharkhand",
    "country": "India",
    "pincode": "834001"
}
```

# 2. Get All Branches:http://127.0.0.1:8000/api/branch/GetAllBranch/
```json
{
    "message": "Branches fetched successfully.",
    "count": 3,
    "data": [
        {
            "id": 2,
            "name": "Jamshedpur Branch",
            "email": "jamshedpur.branch@example.com",
            "phone": "9123456789",
            "pincode": "831001",
            "code": "JAM001",
            "address": "Bistupur Main Road",
            "city": "Jamshedpur",
            "state": "Jharkhand",
            "country": "India",
            "description": "Branch for East Singhbhum churches.",
            "logo": "/branches/logo/WhatsApp_Image_2026-07-31_at_11_8d9avcP.19.12.jpeg",
            "verification_status": "APPROVED",
            "is_active": true,
            "created_at": "2026-08-01T05:04:46.840836Z",
            "updated_at": "2026-08-01T05:04:46.841057Z"
        },
        {
            "id": 1,
            "name": "Ranchi Branch",
            "email": "ranchi.branch@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "RAN005",
            "address": "Main Road, Lalpur",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "Regional branch serving churches across Jharkhand.",
            "logo": "/branches/logo/WhatsApp_Image_2026-07-31_at_11_OWKw9XO.19.12.jpeg",
            "verification_status": "PENDING",
            "is_active": true,
            "created_at": "2026-08-01T04:44:18.822334Z",
            "updated_at": "2026-08-01T06:16:35.030966Z"
        },
        {
            "id": 3,
            "name": "Seraikella Branch",
            "email": "seraikella.branch@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "SER001",
            "address": "Main Road, seraikella",
            "city": "Seraikella",
            "state": "Jharkhand",
            "country": "India",
            "description": "Regional branch serving churches across Jharkhand.",
            "logo": "/branches/logo/WhatsApp_Image_2026-07-31_at_11_o0Gc37D.19.12.jpeg",
            "verification_status": "PENDING",
            "is_active": true,
            "created_at": "2026-08-01T06:07:28.786057Z",
            "updated_at": "2026-08-01T06:07:28.786531Z"
        }
    ]
}
```
# 3. Get Single Branch
# 4. Update Branch:http://127.0.0.1:8000/api/branch/UpdateBranch/1/
```json
query parameters: from-data
{
"email":"ranchi.branch@example.com",
"phone": "9876543210",
"address":"Main Road, Lalpur",
"city":"Ranchi",
"state":"Jharkhand",
"country":"India",
"pincode":"834001",
"description":"Regional branch serving churches across Jharkhand.",
"verification_status":"PENDING",
"is_active":true
}

```
# 5. Delete Branch: http://127.0.0.1:8000/api/branch/DeleteBranch/?id=1
``` json
query parameters:params
id:2
{
    "message": "Branch Deleted successfully.",
    "status": true
}
```
# 6. Approve Branch: http://127.0.0.1:8000/api/branch/ApproveBranch/?id=4
```json
request:-
query parameters:params
id:4
response:-

{
    "message": "Branch Approved Successfully.",
    "data": {
        "id": 4,
        "name": "Seraikella Branch",
        "email": "seraikella.branch@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "SER001",
        "address": "Main Road, seraikella",
        "city": "Seraikella",
        "state": "Jharkhand",
        "country": "India",
        "description": "Regional branch serving churches across Jharkhand.",
        "logo": "/branches/logo/WhatsApp_Image_2026-07-31_at_11_lckr81g.19.12.jpeg",
        "verification_status": "APPROVED",
        "is_active": true,
        "created_at": "2026-08-01T07:32:31.097834Z",
        "updated_at": "2026-08-01T08:02:11.885011Z"
    }
}
```

# 7. Reject Branch: http://127.0.0.1:8000/api/branch/RejectBranch/?Branch_id=5
```json
query parameters:params
Branch_id:5
response:
{
    "message": "This Branch Rejected.",
    "data": {
        "id": 5,
        "name": "Ranchi Branch",
        "email": "ranchi.branch@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "RAN001",
        "address": "Main Road, Lalpur,",
        "city": "Ranchi",
        "state": "Jharkhand",
        "country": "India",
        "description": "Regional branch serving churches across Jharkhand.",
        "logo": "/branches/logo/WhatsApp_Image_2026-07-31_at_11_LIDqhIP.19.12.jpeg",
        "verification_status": "REJECTED",
        "is_active": true,
        "created_at": "2026-08-01T07:33:55.838331Z",
        "updated_at": "2026-08-01T09:20:07.239869Z"
    }
}
```
# 8. Activate Branch
# 9. Deactivate Branch
# 10. Branch Dashboard
# 11. Branch Statistics
# 12. Search Branch
GET /api/branch/GetAllBranch/?search=ranchi
GET /api/branch/GetAllBranch/?city=Ranchi
GET /api/branch/GetAllBranch/?status=APPROVED

{
    "total_branches": 15,
    "approved": 12,
    "pending": 2,
    "rejected": 1
}
# 8. All Pending Branch API: http://127.0.0.1:8000/api/branch/ListOfPendingBranch/
## Method:Get,
## Query parameters:no
- Response:-
```json
{
    "message": "List of Pending Branch",
    "data": [
        {
            "id": 4,
            "name": "Kharswan",
            "email": "kharswan.branch@gmail.com",
            "phone": "7480920155",
            "pincode": "833225",
            "code": "KHAR001",
            "address": "Kharswan",
            "city": "Kharswan",
            "state": "Jharkhand",
            "country": "India",
            "description": "this is kharswan  branch.",
            "logo": "/media/branches/logo/casa-bike_4mi1cBB.com_index.html.png",
            "verification_status": "PENDING",
            "is_active": false,
            "created_at": "2026-08-17T10:05:08.756765Z",
            "updated_at": "2026-08-17T10:05:08.756813Z",
            "user": 23
        }
    ]
}
``` 
# 9. All Approved Branch API:http://127.0.0.1:8000/api/branch/ListOfApprovedBranches/
## Method:GET
## Query Parameters:no
- Response:-
```json
{
    "message": "List of Approved Branch",
    "data": [
        {
            "id": 2,
            "name": "Jamshedpur Branch",
            "email": "jamshedpur.branch@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "JSP00",
            "address": "Main Road, Lalpur",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "Regional branch serving churches across Jharkhand.",
            "logo": "/media/branches/logo/WhatsApp_Image_2026-07-31_at_11_ffoRzLi.19.12.jpeg",
            "verification_status": "APPROVED",
            "is_active": true,
            "created_at": "2026-08-05T07:14:17.974382Z",
            "updated_at": "2026-08-17T09:58:37.987241Z",
            "user": null
        },
        {
            "id": 1,
            "name": "Ranchi Branch",
            "email": "ranchi.branch@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "RAN001",
            "address": "Main Road, Lalpur",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "Regional branch serving churches across Jharkhand.",
            "logo": "/media/branches/logo/WhatsApp_Image_2026-07-31_at_11_LJRgIjy.19.12.jpeg",
            "verification_status": "APPROVED",
            "is_active": true,
            "created_at": "2026-08-05T07:05:24.264212Z",
            "updated_at": "2026-08-17T09:58:31.591357Z",
            "user": null
        },
        {
            "id": 3,
            "name": "seraikella",
            "email": "seraikella.branch@gmail.com",
            "phone": "7480920110",
            "pincode": "833219",
            "code": "SER001",
            "address": "Seraikella",
            "city": "Seraikella",
            "state": "Jharkhand",
            "country": "India",
            "description": "shfhshkhdisuhis",
            "logo": "/media/branches/logo/casa-bike.com_index.html.png",
            "verification_status": "APPROVED",
            "is_active": false,
            "created_at": "2026-08-17T09:57:45.797427Z",
            "updated_at": "2026-08-17T09:58:13.993850Z",
            "user": 22
        }
    ]
}
```