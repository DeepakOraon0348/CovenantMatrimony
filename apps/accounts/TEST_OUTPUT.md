# 1. register user API: http://127.0.0.1:8000/api/auth/CreateAccount/
## Method: POST
## Query Parameters: JSON
- Request:- 
```json
{
    "first_name": "Deepak",
    "last_name": "Oraon",
    "email": "deepak12345@gmail.com",
    "phone": "9876543200",
    "password": "Deepak@123",
    "branch": 1,
    "church": 1
},
{
    "first_name": "Deepak",
    "last_name": "Oraon",
    "email": "deepak@gmail.com",
    "phone": "9876543210",
    "password": "Deepak@123",
    "branch": 1,
    "church": 999
},
{
    "first_name": "Joti",
    "last_name": "Kumari",
    "email": "joti@gmail.com",
    "phone": "9888553515",
    "password": "Joti@123",
    "role":"BRANCH_ADMIN"
},
{
    "first_name": "jti",
    "last_name": "Kumari",
    "email": "jti@gmail.com",
    "phone": "9888563515",
    "password": "Jti@1234",
    "role":"CHURCH_ADMIN"
}
```
- Response:-
```json
{
    "message": "User Register Sucessful.",
    "data": {
        "id": 3,
        "first_name": "Deepak",
        "last_name": "Oraon",
        "email": "deepak12345@gmail.com",
        "phone": "9876543200",
        "last_login": null,
        "is_superuser": false,
        "is_staff": false,
        "date_joined": "2026-08-05T07:37:24.874426Z",
        "role": "USER",
        "is_email_verified": false,
        "is_active": true,
        "is_deleted": false,
        "created_at": "2026-08-05T07:37:24.874977Z",
        "updated_at": "2026-08-05T07:37:24.874985Z",
        "branch": 1,
        "church": 1,
        "groups": [],
        "user_permissions": []
    }
},
{
    "message": "User Register Sucessful.",
    "data": {
        "id": 13,
        "first_name": "Joti",
        "last_name": "Kumari",
        "email": "joti@gmail.com",
        "phone": "9888553515",
        "last_login": null,
        "is_superuser": false,
        "is_staff": false,
        "date_joined": "2026-08-13T12:21:29.035480Z",
        "role": "BRANCH_ADMIN",
        "is_email_verified": false,
        "is_active": true,
        "is_deleted": false,
        "created_at": "2026-08-13T12:21:30.141156Z",
        "updated_at": "2026-08-13T12:21:30.141187Z",
        "branch": null,
        "church": null,
        "groups": [],
        "user_permissions": []
    }
},
{
    "message": "User Register Sucessful.",
    "data": {
        "id": 14,
        "first_name": "jti",
        "last_name": "Kumari",
        "email": "jti@gmail.com",
        "phone": "9888563515",
        "last_login": null,
        "is_superuser": false,
        "is_staff": false,
        "date_joined": "2026-08-13T12:25:28.906803Z",
        "role": "CHURCH_ADMIN",
        "is_email_verified": false,
        "is_active": true,
        "is_deleted": false,
        "created_at": "2026-08-13T12:25:30.258323Z",
        "updated_at": "2026-08-13T12:25:30.258339Z",
        "branch": null,
        "church": null,
        "groups": [],
        "user_permissions": []
    }
},
{
    "email": [
        "Email already exists."
    ],
    "phone": [
        "Phone number already exists."
    ],
    "church": [
        "Invalid pk \"999\" - object does not exist."
    ]
}
```

# 2. User Login API: http://127.0.0.1:8000/api/auth/UserLogin/
## Method: POST
## Query Parameters: JSON
- Request:-
```json
{
 "email": "rahul@gmail.com",
 "password": "Rahul@123"
}
```
- Response:-
```json
{
    "message": "Login Successful.",
    "data": {
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg1OTIwMjA5LCJpYXQiOjE3ODU5MTg0MDksImp0aSI6IjA0MWQ1MTcwNGIzNzRhNmVhNjI4ZWRhZGViNzY3OWExIiwidXNlcl9pZCI6IjUifQ.l57R_6btpJ90VrdzSNdpWeBcWl_NfsfDn26BYiS9VsM",
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc4NjUyMzIwOSwiaWF0IjoxNzg1OTE4NDA5LCJqdGkiOiI5NzI0YTYwMWJkODA0YzNmOTNlM2RlYjJlNTM5YzNhYSIsInVzZXJfaWQiOiI1In0.d_zH5skvUsRllnwXC1GbzSbAltqXssENGDEmHtjwASw",
        "user": {
            "id": 5,
            "first_name": "Rahul",
            "last_name": "Kumar",
            "email": "rahul@gmail.com",
            "phone": "9876543111",
            "role": "USER",
            "branch": 1,
            "church": 1
        }
    }
}
```

# 3. Get All Register user API: http://127.0.0.1:8000/api/auth/GetAllRegisterUser/ 

## Method: GET,
## Query parameters: no
- Response:-
```json
{
    "message": "Get All Register User.",
    "data": [
        {
            "id": 1,
            "first_name": "Deepak",
            "last_name": "Oraon",
            "email": "deepak@gmail.com",
            "phone": "9876543210",
            "last_login": null,
            "is_superuser": false,
            "is_staff": false,
            "date_joined": "2026-08-05T07:33:30.445655Z",
            "role": "USER",
            "is_email_verified": false,
            "is_active": true,
            "is_deleted": false,
            "created_at": "2026-08-05T07:33:30.452536Z",
            "updated_at": "2026-08-05T07:33:30.452569Z",
            "branch": 1,
            "church": 1,
            "groups": [],
            "user_permissions": []
        },
        {
            "id": 2,
            "first_name": "Deepak",
            "last_name": "Oraon",
            "email": "deepak12@gmail.com",
            "phone": "9876543201",
            "last_login": null,
            "is_superuser": false,
            "is_staff": false,
            "date_joined": "2026-08-05T07:34:57.021114Z",
            "role": "USER",
            "is_email_verified": false,
            "is_active": true,
            "is_deleted": false,
            "created_at": "2026-08-05T07:34:57.021553Z",
            "updated_at": "2026-08-05T07:34:57.021568Z",
            "branch": 1,
            "church": 1,
            "groups": [],
            "user_permissions": []
        },
        {
            "id": 3,
            "first_name": "Deepak",
            "last_name": "Oraon",
            "email": "deepak12345@gmail.com",
            "phone": "9876543200",
            "last_login": null,
            "is_superuser": false,
            "is_staff": false,
            "date_joined": "2026-08-05T07:37:24.874426Z",
            "role": "USER",
            "is_email_verified": false,
            "is_active": true,
            "is_deleted": false,
            "created_at": "2026-08-05T07:37:24.874977Z",
            "updated_at": "2026-08-05T07:37:24.874985Z",
            "branch": 1,
            "church": 1,
            "groups": [],
            "user_permissions": []
        },
        {
            "id": 4,
            "first_name": "Deepak",
            "last_name": "Oraon",
            "email": "deepak9797@gmail.com",
            "phone": "9876543222",
            "last_login": null,
            "is_superuser": false,
            "is_staff": false,
            "date_joined": "2026-08-05T08:13:51.379088Z",
            "role": "USER",
            "is_email_verified": false,
            "is_active": true,
            "is_deleted": false,
            "created_at": "2026-08-05T08:13:51.379393Z",
            "updated_at": "2026-08-05T08:13:51.379402Z",
            "branch": 1,
            "church": 1,
            "groups": [],
            "user_permissions": []
        },
        {
            "id": 5,
            "first_name": "Rahul",
            "last_name": "Kumar",
            "email": "rahul@gmail.com",
            "phone": "9876543111",
            "last_login": null,
            "is_superuser": false,
            "is_staff": false,
            "date_joined": "2026-08-05T08:25:21.551750Z",
            "role": "USER",
            "is_email_verified": false,
            "is_active": true,
            "is_deleted": false,
            "created_at": "2026-08-05T08:25:22.118213Z",
            "updated_at": "2026-08-05T08:25:22.118221Z",
            "branch": 1,
            "church": 1,
            "groups": [],
            "user_permissions": []
        }
    ]
}
```

# 4. Get Total Numbers of user API: http://127.0.0.1:8000/api/auth/NumbersOfRegisterUser/
## Method: GET
## Query Parameters: no

- Response:-
```json
{
    "message": "Total Numbers of Register Users.",
    "total": 5
}
```
# 5. get user Dashboard: http://127.0.0.1:8000/api/auth/MyDashboard/
## Method: GET
## Query parameters: onlu user login required.
- Response:-
```json
{
    "message": "Dashboard data fetched successfully.",
    "data": {
        "profile": {
            "id": 4,
            "profile_id": "MAT000004",
            "height": "5.8",
            "weight": 68,
            "education": "B.Tech",
            "occupation": "Software Engineer",
            "annual_income": "800000.00",
            "about_me": "I am a software engineer looking for a life partner.",
            "profile_type": "GROOM",
            "gender": "MALE",
            "date_of_birth": "1999-05-10",
            "marital_status": "UNMARRIED",
            "profile_photo": "/profiles/photos/WhatsApp_Image_2026-07-31_at_11.19.12.jpeg",
            "is_profile_completed": false,
            "profile_status": "VERIFIED",
            "is_photo_visible": true,
            "is_verified": true,
            "is_active": true,
            "created_at": "2026-08-08T07:02:30.995540Z",
            "updated_at": "2026-08-13T05:51:02.079972Z",
            "user": 7,
            "denomination": 1
        },
        "subscription": {
            "id": 3,
            "plan": 2,
            "start_date": "2026-08-13T05:51:02.034735Z",
            "expiry_date": "2026-09-12T05:51:02.034735Z",
            "is_active": true,
            "created_at": "2026-08-13T05:51:02.054161Z",
            "updated_at": "2026-08-13T05:51:02.054195Z",
            "user": 7
        },
        "interests": {
            "sent": [
                {
                    "id": 1,
                    "sender_profile": 4,
                    "receiver_profile": 2,
                    "status": "REJECTED",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-12T10:31:20.997180Z",
                    "updated_at": "2026-08-12T18:22:36.330268Z"
                },
                {
                    "id": 2,
                    "sender_profile": 4,
                    "receiver_profile": 3,
                    "status": "PENDING",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-12T10:35:20.535888Z",
                    "updated_at": "2026-08-12T10:35:20.536572Z"
                }
            ],
            "received": [
                {
                    "id": 3,
                    "sender_profile": 6,
                    "receiver_profile": 4,
                    "status": "ACCEPTED",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-12T10:55:53.251008Z",
                    "updated_at": "2026-08-12T12:18:57.904456Z"
                },
                {
                    "id": 4,
                    "sender_profile": 7,
                    "receiver_profile": 4,
                    "status": "REJECTED",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-12T12:33:36.751587Z",
                    "updated_at": "2026-08-12T17:54:44.348081Z"
                },
                {
                    "id": 5,
                    "sender_profile": 8,
                    "receiver_profile": 4,
                    "status": "ACCEPTED",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-13T07:29:21.524530Z",
                    "updated_at": "2026-08-13T07:29:56.578437Z"
                },
                {
                    "id": 6,
                    "sender_profile": 9,
                    "receiver_profile": 4,
                    "status": "ACCEPTED",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-13T08:05:24.195987Z",
                    "updated_at": "2026-08-13T08:06:21.225850Z"
                },
                {
                    "id": 7,
                    "sender_profile": 10,
                    "receiver_profile": 4,
                    "status": "ACCEPTED",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-13T09:16:53.209584Z",
                    "updated_at": "2026-08-13T09:18:21.566380Z"
                }
            ]
        },
        "matches": [
            {
                "id": 1,
                "interest_request": {
                    "id": 3,
                    "sender_profile": 6,
                    "receiver_profile": 4,
                    "status": "ACCEPTED",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-12T10:55:53.251008Z",
                    "updated_at": "2026-08-12T12:18:57.904456Z"
                },
                "status": "CLOSED",
                "matched_at": "2026-08-12T12:18:57.928217Z",
                "updated_at": "2026-08-12T19:05:53.603157Z"
            },
            {
                "id": 2,
                "interest_request": {
                    "id": 5,
                    "sender_profile": 8,
                    "receiver_profile": 4,
                    "status": "ACCEPTED",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-13T07:29:21.524530Z",
                    "updated_at": "2026-08-13T07:29:56.578437Z"
                },
                "status": "ACTIVE",
                "matched_at": "2026-08-13T07:29:56.581533Z",
                "updated_at": "2026-08-13T07:29:56.581552Z"
            },
            {
                "id": 3,
                "interest_request": {
                    "id": 6,
                    "sender_profile": 9,
                    "receiver_profile": 4,
                    "status": "ACCEPTED",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-13T08:05:24.195987Z",
                    "updated_at": "2026-08-13T08:06:21.225850Z"
                },
                "status": "ACTIVE",
                "matched_at": "2026-08-13T08:06:21.228861Z",
                "updated_at": "2026-08-13T08:06:21.228892Z"
            },
            {
                "id": 4,
                "interest_request": {
                    "id": 7,
                    "sender_profile": 10,
                    "receiver_profile": 4,
                    "status": "ACCEPTED",
                    "message": "I am interested in your profile.",
                    "created_at": "2026-08-13T09:16:53.209584Z",
                    "updated_at": "2026-08-13T09:18:21.566380Z"
                },
                "status": "ACTIVE",
                "matched_at": "2026-08-13T09:18:21.571521Z",
                "updated_at": "2026-08-13T09:18:21.571571Z"
            }
        ],
        "meetings": [
            {
                "id": 1,
                "match": 2,
                "meeting_date": "2026-08-20",
                "meeting_time": "18:30:00",
                "venue": "St. Mary's Church, Ranchi",
                "status": "SCHEDULED",
                "remarks": "First meeting between both families.",
                "created_at": "2026-08-13T07:30:49.796373Z",
                "updated_at": "2026-08-13T07:30:49.796411Z"
            },
            {
                "id": 2,
                "match": 3,
                "meeting_date": "2026-08-30",
                "meeting_time": "18:30:00",
                "venue": "St. Mary's Church, Ranchi",
                "status": "CANCELLED",
                "remarks": "First meeting between both families.",
                "created_at": "2026-08-13T08:07:16.665308Z",
                "updated_at": "2026-08-13T08:28:22.319985Z"
            },
            {
                "id": 3,
                "match": 4,
                "meeting_date": "2026-08-22",
                "meeting_time": "18:30:00",
                "venue": "St. Mary's Church, Ranchi",
                "status": "COMPLETED",
                "remarks": "First meeting between both families.",
                "created_at": "2026-08-13T09:20:02.934942Z",
                "updated_at": "2026-08-13T09:54:26.176544Z"
            }
        ],
        "marriages": [
            {
                "id": 1,
                "meeting": 3,
                "marriage_date": "2026-09-20",
                "venue": "St. Mary's Church, Ranchi",
                "pastor_name": "Pastor John",
                "status": "COMPLETED",
                "remarks": "Marriage ceremony scheduled successfully.",
                "created_at": "2026-08-13T09:57:20.313112Z",
                "updated_at": "2026-08-13T10:46:46.779636Z"
            }
        ],
        "prayers": [
            {
                "id": 2,
                "church": 1,
                "church_name": "St. Peter Church",
                "created_by": 7,
                "created_by_name": "Sanju Sardar",
                "title": "Prayer for Church Members",
                "note": "Please pray for the health, peace and spiritual growth of all church members.",
                "status": "ONGOING",
                "created_at": "2026-08-14T08:32:31.435834Z",
                "completed_at": null,
                "updated_at": "2026-08-14T08:32:31.435985Z"
            }
        ],
        "document": [
            {
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
        ],
        "family": [
            {
                "id": 2,
                "father_name": "Ramesh Oraon",
                "mother_name": "Sunita Oraon",
                "father_occupation": "Government Employee",
                "mother_occupation": "Teacher",
                "brothers": 1,
                "sisters": 2,
                "family_type": "NUCLEAR",
                "created_at": "2026-08-14T08:30:10.277737Z",
                "updated_at": "2026-08-14T08:30:10.278882Z",
                "profile": 4
            }
        ]
    }
}
```