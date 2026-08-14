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
# 5. 