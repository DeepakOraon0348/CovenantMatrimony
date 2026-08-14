# 1. Create Church API: http://127.0.0.1:8000/api/churches/createChurch/
## Method: POST
## query parameters:from-data
- req:-
```json
{
    "branch": 5,
    "name": "St. Peter Church",
    "code": "STP001",
    "email": "stpeter@gmail.com",
    "phone": "9876543210",
    "pastor_name": "Rev. John Lakra",
    "address": "Main Road, Ranchi",
    "city": "Ranchi",
    "state": "Jharkhand",
    "country": "India",
    "pincode": "834001"
}
```
- Response
```json
{
    "message": "Church created successfully.",
    "data": {
        "id": 2,
        "name": "St. Poll Church",
        "pastor_name": "Rev. John kshyap",
        "email": "stpeter12@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "STP002",
        "address": "Bhubajar",
        "city": "Ranchi",
        "state": "Jharkhand",
        "country": "India",
        "description": "A Roman Catholic church serving the Ranchi community.",
        "logo": null,
        "verification_status": "PENDING",
        "is_active": true,
        "created_at": "2026-08-03T09:31:48.793913Z",
        "updated_at": "2026-08-03T09:31:48.793951Z",
        "branch": 6
    }
}

```

# 2. Update Church API: http://127.0.0.1:8000/api/churches/updateChurch/2/

## Method: POST

## query parameters:from-data
- Request 
```json
{
"branch":6,
"name":"St.Poll Church-1",
"code":STP002,
"email":"stpeter1234@example.com",
"phone":9876543210,
"address":"Bhubajar",
"city":"Ranchi",
"state":"Jharkhand",
"country":"India",
"pincode":834001,
"pastor_name":"Rev. John kshyap",
"description":"A Roman Catholic church serving the Ranchi community.",
"verification_status":"PENDING"
"is_active":true
}
```
- Response:-
``` json
{
    "message": "Church updated successfully.",
    "data": {
        "id": 2,
        "name": "St. Poll Church-1",
        "pastor_name": "Rev. John kshyap",
        "email": "stpeter1234@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "STP002",
        "address": "Bhubajar",
        "city": "Ranchi",
        "state": "Jharkhand",
        "country": "India",
        "description": "A Roman Catholic church serving the Ranchi community.",
        "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11.19.12.jpeg",
        "verification_status": "PENDING",
        "is_active": true,
        "created_at": "2026-08-03T09:31:48.793913Z",
        "updated_at": "2026-08-03T09:50:49.709384Z",
        "branch": 6
    }
}
```
# 3. Get All Church: http://127.0.0.1:8000/api/churches/getAllChurches/
##  Method: Get.
- Response:-
```json
{
    "message": "All churches retrieved successfully.",
    "total": 2,
    "data": [
        {
            "id": 1,
            "name": "St. Poll Church",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP001",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": null,
            "verification_status": "PENDING",
            "is_active": true,
            "created_at": "2026-08-03T09:02:20.014070Z",
            "updated_at": "2026-08-03T09:05:18.407496Z",
            "branch": 6
        },
        {
            "id": 2,
            "name": "St. Poll Church-1",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter1234@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP002",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11.19.12.jpeg",
            "verification_status": "PENDING",
            "is_active": true,
            "created_at": "2026-08-03T09:31:48.793913Z",
            "updated_at": "2026-08-03T09:50:49.709384Z",
            "branch": 6
        }
    ]
}
```

# 4. Get Church By Id: http://127.0.0.1:8000/api/churches/getChurchById/?church_id=2
## Method: POST
## query parameters:Prams
- request:- 
```json
{
    "church_id": 2
}
``` 
- Response:-
```json
{
    "message": "Church retrieved successfully.",
    "data": {
        "id": 2,
        "name": "St. Poll Church-1",
        "pastor_name": "Rev. John kshyap",
        "email": "stpeter1234@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "STP002",
        "address": "Bhubajar",
        "city": "Ranchi",
        "state": "Jharkhand",
        "country": "India",
        "description": "A Roman Catholic church serving the Ranchi community.",
        "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11.19.12.jpeg",
        "verification_status": "PENDING",
        "is_active": true,
        "created_at": "2026-08-03T09:31:48.793913Z",
        "updated_at": "2026-08-03T09:50:49.709384Z",
        "branch": 6
    }
}
```

# 5 Delete church API: http://127.0.0.1:8000/api/churches/deleteChurch/?church_id=2
## Method: delete
## query parameters:Prams
- Request:-
```json
{
    "church_id":2,
}
```
- Response:- 
``` json
{
    "message": "Church deleted successfully.",
    "status": true
}
```

# 6. Church Approved by Supper Admin API: http://127.0.0.1:8000/api/churches/approveChurch/?church_id=3

## Method: POST
## query parameters:Prams

- Request:-
```json
{
    "church_id": 3,
}
```

- Response:-
``` json
{
    "message": "Church approved successfully.",
    "data": {
        "id": 3,
        "name": "St. Poll Church12",
        "pastor_name": "Rev. John kshyap",
        "email": "stpeter1245@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "STP003",
        "address": "Bhubajar",
        "city": "Ranchi",
        "state": "Jharkhand",
        "country": "India",
        "description": "A Roman Catholic church serving the Ranchi community.",
        "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11.19.12_3.jpeg",
        "verification_status": "APPROVED",
        "is_active": true,
        "created_at": "2026-08-03T11:40:23.384866Z",
        "updated_at": "2026-08-03T11:46:59.926209Z",
        "branch": 6
    }
}
```

# 7. Church Rejected through id by Supper Admin API: http://127.0.0.1:8000/api/churches/rejectChurch/?church_id=1

## Method: POST
## query parameters:Prams

- Request:-
``` json
{
    "church_id": 2,
}
```
- Response:-
```json
{
    "message": "Church rejected successfully.",
    "data": {
        "id": 1,
        "name": "St. Poll Church",
        "pastor_name": "Rev. John kshyap",
        "email": "stpeter@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "STP001",
        "address": "Bhubajar",
        "city": "Ranchi",
        "state": "Jharkhand",
        "country": "India",
        "description": "A Roman Catholic church serving the Ranchi community.",
        "logo": null,
        "verification_status": "REJECTED",
        "is_active": true,
        "created_at": "2026-08-03T09:02:20.014070Z",
        "updated_at": "2026-08-03T11:46:41.570434Z",
        "branch": 6
    }
}
```

# 9. Get All Approved Church API: http://127.0.0.1:8000/api/churches/getApprovedChurches/   
## Method: get
## Query Parameters: no

- Response:-
```json
{
    "message": "Approved churches retrieved successfully.",
    "total": 1,
    "data": [
        {
            "id": 3,
            "name": "St. Poll Church12",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter1245@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP003",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11.19.12_3.jpeg",
            "verification_status": "APPROVED",
            "is_active": true,
            "created_at": "2026-08-03T11:40:23.384866Z",
            "updated_at": "2026-08-03T11:46:59.926209Z",
            "branch": 6
        }
    ]
}
```

# 10. get all Rejected church API: http://127.0.0.1:8000/api/churches/getAllRejectedChurches/
## Method : Get
##  query parameters: no
- Response:-
```json
{
    "message": "Rejected churches retrieved successfully.",
    "total": 1,
    "data": [
        {
            "id": 1,
            "name": "St. Poll Church",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP001",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": null,
            "verification_status": "REJECTED",
            "is_active": true,
            "created_at": "2026-08-03T09:02:20.014070Z",
            "updated_at": "2026-08-03T11:46:41.570434Z",
            "branch": 6
        }
    ]
}
```

# 11. Get All Pending Church API: http://127.0.0.1:8000/api/churches/getAllPendingChurches/
## Method : Get
## query parameters: no

- Response
```json
{
    "message": "Pending churches retrieved successfully.",
    "total": 2,
    "data": [
        {
            "id": 4,
            "name": "St. Poll12",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter12456@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP004",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11_jP0nESB.19.12_3.jpeg",
            "verification_status": "PENDING",
            "is_active": true,
            "created_at": "2026-08-03T11:40:59.616132Z",
            "updated_at": "2026-08-03T11:40:59.616176Z",
            "branch": 6
        },
        {
            "id": 5,
            "name": "St. Poll123",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter124567@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP005",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11_yuAY3Y8.19.12_3.jpeg",
            "verification_status": "PENDING",
            "is_active": true,
            "created_at": "2026-08-03T11:41:25.500955Z",
            "updated_at": "2026-08-03T11:41:25.500999Z",
            "branch": 6
        }
    ]
}
```

# 12. church activation api : http://127.0.0.1:8000/api/churches/activateChurch/?church_id=1
## Method: Post
## query parameters: parms
- Request:-
```json
{
    " church_id": 2,
}
```
- Response:- 
```json
{
    "message": "Church activated successfully.",
    "data": {
        "id": 1,
        "name": "St. Poll Church",
        "pastor_name": "Rev. John kshyap",
        "email": "stpeter@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "STP001",
        "address": "Bhubajar",
        "city": "Ranchi",
        "state": "Jharkhand",
        "country": "India",
        "description": "A Roman Catholic church serving the Ranchi community.",
        "logo": null,
        "verification_status": "REJECTED",
        "is_active": true,
        "created_at": "2026-08-03T09:02:20.014070Z",
        "updated_at": "2026-08-03T12:24:10.155463Z",
        "branch": 6
    }
}
```

# 13. Church Inactivation API: http://127.0.0.1:8000/api/churches/deactivateChurch/?church_id=1
## Method: POST
## Query parameters: params
- Request:-
```json
{
    "church_id":1,
}
```
- Response:-
```json
{
    "message": "Church deactivated successfully.",
    "data": {
        "id": 1,
        "name": "St. Poll Church",
        "pastor_name": "Rev. John kshyap",
        "email": "stpeter@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "STP001",
        "address": "Bhubajar",
        "city": "Ranchi",
        "state": "Jharkhand",
        "country": "India",
        "description": "A Roman Catholic church serving the Ranchi community.",
        "logo": null,
        "verification_status": "REJECTED",
        "is_active": false,
        "created_at": "2026-08-03T09:02:20.014070Z",
        "updated_at": "2026-08-04T04:46:37.916349Z",
        "branch": 6
    }
}
```

# 14. List of Active church API: http://127.0.0.1:8000/api/churches/getListOfActiveChurches/
## Method: get
## query parameters: no
- Response:-
```json
{
    "message": "Active churches retrieved successfully.",
    "total": 3,
    "data": [
        {
            "id": 3,
            "name": "St. Poll Church12",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter1245@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP003",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11.19.12_3.jpeg",
            "verification_status": "APPROVED",
            "is_active": true,
            "created_at": "2026-08-03T11:40:23.384866Z",
            "updated_at": "2026-08-03T11:46:59.926209Z",
            "branch": 6
        },
        {
            "id": 4,
            "name": "St. Poll12",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter12456@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP004",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11_jP0nESB.19.12_3.jpeg",
            "verification_status": "PENDING",
            "is_active": true,
            "created_at": "2026-08-03T11:40:59.616132Z",
            "updated_at": "2026-08-03T11:40:59.616176Z",
            "branch": 6
        },
        {
            "id": 5,
            "name": "St. Poll123",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter124567@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP005",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11_yuAY3Y8.19.12_3.jpeg",
            "verification_status": "PENDING",
            "is_active": true,
            "created_at": "2026-08-03T11:41:25.500955Z",
            "updated_at": "2026-08-03T11:41:25.500999Z",
            "branch": 6
        }
    ]
}
```
# 15. Get Total number of chuch API: http://127.0.0.1:8000/api/churches/numberOfChurches/
## Methos: Get
## Query parameters: no,

- Response:-
```json
{
    "message": "Total number of churches retrieved successfully.",
    "total": 4
}
```
# 16. Get all inactive church/ get total numbers of inactive church API: http://127.0.0.1:8000/api/churches/getListOfInactiveChurches/

## Method: get
## query parameters: no

- response:-
```json
{
    "message": "Inactive churches retrieved successfully.",
    "total": 1,
    "data": [
        {
            "id": 1,
            "name": "St. Poll Church",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP001",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": null,
            "verification_status": "REJECTED",
            "is_active": false,
            "created_at": "2026-08-03T09:02:20.014070Z",
            "updated_at": "2026-08-04T04:46:37.916349Z",
            "branch": 6
        }
    ]
}
```

# 17. Get Church by Branch id API: http://127.0.0.1:8000/api/churches/getChurchByBranchId/?branch_id=6

## Method: Get
## Query parameters: params
- Request:-
```json
{
    "branch_id":6,
}
```

- Response:-
``` json
{
    "message": "Churches retrieved successfully.",
    "total": 4,
    "data": [
        {
            "id": 1,
            "name": "St. Poll Church",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP001",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": null,
            "verification_status": "REJECTED",
            "is_active": false,
            "created_at": "2026-08-03T09:02:20.014070Z",
            "updated_at": "2026-08-04T04:46:37.916349Z",
            "branch": 6
        },
        {
            "id": 3,
            "name": "St. Poll Church12",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter1245@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP003",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11.19.12_3.jpeg",
            "verification_status": "APPROVED",
            "is_active": true,
            "created_at": "2026-08-03T11:40:23.384866Z",
            "updated_at": "2026-08-03T11:46:59.926209Z",
            "branch": 6
        },
        {
            "id": 4,
            "name": "St. Poll12",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter12456@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP004",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11_jP0nESB.19.12_3.jpeg",
            "verification_status": "PENDING",
            "is_active": true,
            "created_at": "2026-08-03T11:40:59.616132Z",
            "updated_at": "2026-08-03T11:40:59.616176Z",
            "branch": 6
        },
        {
            "id": 5,
            "name": "St. Poll123",
            "pastor_name": "Rev. John kshyap",
            "email": "stpeter124567@example.com",
            "phone": "9876543210",
            "pincode": "834001",
            "code": "STP005",
            "address": "Bhubajar",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "description": "A Roman Catholic church serving the Ranchi community.",
            "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11_yuAY3Y8.19.12_3.jpeg",
            "verification_status": "PENDING",
            "is_active": true,
            "created_at": "2026-08-03T11:41:25.500955Z",
            "updated_at": "2026-08-03T11:41:25.500999Z",
            "branch": 6
        }
    ]
}
```

# 18. search the church with different parameters API: http://127.0.0.1:8000/api/churches/searchChurches/?city=Ranchi&name=St. Poll12&pastor_name=Rev. John kshyap

## Methods: Get
## query parameters: params
- Request:
```json
{
    "city":"Ranchi",
    "name":"St. Poll12",
    "code":STP005,
    "pastor_name":"Rev. John kshyap"
}
```

- Response:-
```json
[
    {
        "id": 4,
        "name": "St. Poll12",
        "pastor_name": "Rev. John kshyap",
        "email": "stpeter12456@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "STP004",
        "address": "Bhubajar",
        "city": "Ranchi",
        "state": "Jharkhand",
        "country": "India",
        "description": "A Roman Catholic church serving the Ranchi community.",
        "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11_jP0nESB.19.12_3.jpeg",
        "verification_status": "PENDING",
        "is_active": true,
        "created_at": "2026-08-03T11:40:59.616132Z",
        "updated_at": "2026-08-03T11:40:59.616176Z",
        "branch": 6
    },
    {
        "id": 5,
        "name": "St. Poll123",
        "pastor_name": "Rev. John kshyap",
        "email": "stpeter124567@example.com",
        "phone": "9876543210",
        "pincode": "834001",
        "code": "STP005",
        "address": "Bhubajar",
        "city": "Ranchi",
        "state": "Jharkhand",
        "country": "India",
        "description": "A Roman Catholic church serving the Ranchi community.",
        "logo": "/churches/logo/WhatsApp_Image_2026-07-31_at_11_yuAY3Y8.19.12_3.jpeg",
        "verification_status": "PENDING",
        "is_active": true,
        "created_at": "2026-08-03T11:41:25.500955Z",
        "updated_at": "2026-08-03T11:41:25.500999Z",
        "branch": 6
    }
]
```


