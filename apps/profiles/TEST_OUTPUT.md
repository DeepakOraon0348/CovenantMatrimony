# 1. Create Profile API: http://127.0.0.1:8000/api/profiles/CreateProfile/
## Method: POST
## Query Parameters: JSON
- Request:-
```json
{
    "user": 1,
    "profile_type": "GROOM",
    "gender": "MALE",
    "date_of_birth": "1999-05-10",
    "denomination": 1,
    "marital_status": "UNMARRIED",
    "height": "5.8",
    "weight": 68,
    "education": "B.Tech",
    "occupation": "Software Engineer",
    "annual_income": "800000",
    "about_me": "I am a software engineer looking for a life partner.",
    "profile_photo": null
}
```
- Response:-
```json
{
    "message": "Church created successfully.",
    "data": {
        "id": 1,
        "profile_id": "MAT000001",
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
        "profile_photo": null,
        "is_profile_completed": false,
        "profile_status": "NEW",
        "is_photo_visible": false,
        "is_verified": false,
        "is_active": true,
        "created_at": "2026-08-05T12:22:53.844903Z",
        "updated_at": "2026-08-05T12:22:53.844937Z",
        "user": 1,
        "denomination": 1
    }
}
```

# 2. Update Profile API: http://127.0.0.1:8000/api/profiles/updateProfile/2/
## Method: PUT
## Query Parameters: JSON
- Request:-
```json
{
    "user": 2,
    "profile_type": "BRIDE",
    "gender": "FEMALE",
    "date_of_birth": "2000-05-10",
    "denomination": 1,
    "marital_status": "UNMARRIED",
    "height": "5.8",
    "weight": 68,
    "education": "B.Tech",
    "occupation": "Software Engineer",
    "annual_income": "800000",
    "about_me": "I am a software engineer looking for a life partner.",
    "profile_photo": null
}
```
- Response:-
```json
{
    "message": "Profile updated successfully.",
    "data": {
        "id": 2,
        "height": "5.8",
        "weight": 68,
        "education": "B.Tech",
        "occupation": "Software Engineer",
        "annual_income": "800000.00",
        "about_me": "I am a software engineer looking for a life partner.",
        "profile_id": "MAT000002",
        "profile_type": "BRIDE",
        "gender": "FEMALE",
        "date_of_birth": "2000-05-10",
        "marital_status": "UNMARRIED",
        "profile_photo": null,
        "is_profile_completed": false,
        "profile_status": "NEW",
        "is_photo_visible": false,
        "is_verified": false,
        "is_active": true,
        "created_at": "2026-08-06T05:12:55.647087Z",
        "updated_at": "2026-08-06T05:24:50.048955Z",
        "user": 2,
        "denomination": 1
    }
}
```
# 3. Delete Profile API: http://127.0.0.1:8000/api/profiles/deleteProfile/?profile_id=1
## Method: Delete
## Query Parameters: Params
- Request:-
```json
{
    "profile_id":1,
}
```
- Response:-
```json
{
    "message": "Profile deleted successfully.",
    "Status": true
}
```

# 4. Get my Profile:http://127.0.0.1:8000/api/profiles/getMyProfile/
## Method: GET, 
## Query Parameters: no
```txt
after user Login you have to store these data
localStorage.setItem("access", response.data.data.access);
localStorage.setItem("refresh", response.data.data.refresh);
 
and send with this api:-
const token = localStorage.getItem("access");

fetch("http://127.0.0.1:8000/api/profiles/getMyProfile/", {
    method: "GET",
    headers: {
        Authorization: `Bearer ${token}`,
    },
});
like this.
Header,
Authorization: Bearer <access_token>
```
- Response:-
```json
{
    "message": "Profile fetched successfully.",
    "data": {
        "id": 3,
        "profile_id": "MAT000003",
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
        "profile_photo": null,
        "is_profile_completed": false,
        "profile_status": "NEW",
        "is_photo_visible": false,
        "is_verified": false,
        "is_active": true,
        "created_at": "2026-08-06T06:07:27.871230Z",
        "updated_at": "2026-08-06T06:07:27.871259Z",
        "user": 6,
        "denomination": 1
    }
}
```

# 5. get profile by Id API: http://127.0.0.1:8000/api/profiles/GetProfileById/?profile_id=2
## method: get
## Query Parameters: params,
- Reqeust:-
```json
{
    "profile_id":4,
    "profile_id":2
}
```
- Response:-
```json
{
    "message": "Get Profile by id.",
    "data": {
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
        "profile_photo": null,
        "is_profile_completed": false,
        "profile_status": "NEW",
        "is_photo_visible": false,
        "is_verified": false,
        "is_active": true,
        "created_at": "2026-08-08T07:02:30.995540Z",
        "updated_at": "2026-08-08T07:02:30.995588Z",
        "user": 7,
        "denomination": 1
    },
    {
    "message": "Get Profile by id.",
    "data": {
        "id": 2,
        "profile_id": "MAT000002",
        "height": "5.8",
        "weight": 68,
        "education": "B.Tech",
        "occupation": "Software Engineer",
        "annual_income": "800000.00",
        "about_me": "I am a software engineer looking for a life partner.",
        "profile_type": "BRIDE",
        "gender": "FEMALE",
        "date_of_birth": "2000-05-10",
        "marital_status": "UNMARRIED",
        "profile_photo": null,
        "is_profile_completed": false,
        "profile_status": "NEW",
        "is_photo_visible": false,
        "is_verified": false,
        "is_active": true,
        "created_at": "2026-08-06T05:12:55.647087Z",
        "updated_at": "2026-08-06T05:24:50.048955Z",
        "user": 2,
        "denomination": 1
    }
}
}
```
# 6. Get Active Profile API: http://127.0.0.1:8000/api/profiles/GetAllProfile/
## Method: GET
## Query Parameters: no
- Response:-
```json
{
    "message": "Get all profiles.",
    "total": 3,
    "data": [
        {
            "id": 2,
            "profile_id": "MAT000002",
            "height": "5.8",
            "weight": 68,
            "education": "B.Tech",
            "occupation": "Software Engineer",
            "annual_income": "800000.00",
            "about_me": "I am a software engineer looking for a life partner.",
            "profile_type": "BRIDE",
            "gender": "FEMALE",
            "date_of_birth": "2000-05-10",
            "marital_status": "UNMARRIED",
            "profile_photo": null,
            "is_profile_completed": false,
            "profile_status": "NEW",
            "is_photo_visible": false,
            "is_verified": false,
            "is_active": true,
            "created_at": "2026-08-06T05:12:55.647087Z",
            "updated_at": "2026-08-06T05:24:50.048955Z",
            "user": 2,
            "denomination": 1
        },
        {
            "id": 3,
            "profile_id": "MAT000003",
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
            "profile_photo": null,
            "is_profile_completed": false,
            "profile_status": "NEW",
            "is_photo_visible": false,
            "is_verified": false,
            "is_active": true,
            "created_at": "2026-08-06T06:07:27.871230Z",
            "updated_at": "2026-08-06T06:07:27.871259Z",
            "user": 6,
            "denomination": 1
        },
        {
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
            "profile_photo": null,
            "is_profile_completed": false,
            "profile_status": "NEW",
            "is_photo_visible": false,
            "is_verified": false,
            "is_active": true,
            "created_at": "2026-08-08T07:02:30.995540Z",
            "updated_at": "2026-08-08T07:02:30.995588Z",
            "user": 7,
            "denomination": 1
        }
    ]
}
```

# 7. get in active Profile API:http://127.0.0.1:8000/api/profiles/GetInActiveProfile/
## METHOD: get,
## query parameters: no
- Response:-
```json
{
    "message": "All Inactive profile retrieved successfully.",
    "total": 1,
    "InactiveProfile": [
        {
            "id": 2,
            "profile_id": "MAT000002",
            "height": "5.8",
            "weight": 68,
            "education": "B.Tech",
            "occupation": "Software Engineer",
            "annual_income": "800000.00",
            "about_me": "I am a software engineer looking for a life partner.",
            "profile_type": "BRIDE",
            "gender": "FEMALE",
            "date_of_birth": "2000-05-10",
            "marital_status": "UNMARRIED",
            "profile_photo": null,
            "is_profile_completed": false,
            "profile_status": "NEW",
            "is_photo_visible": false,
            "is_verified": false,
            "is_active": false,
            "created_at": "2026-08-06T05:12:55.647087Z",
            "updated_at": "2026-08-08T08:05:52.981623Z",
            "user": 2,
            "denomination": 1
        }
    ]
}
``` 
# 8. make inactive profile API : http://127.0.0.1:8000/api/profiles/MakeInactiveProfile/?profile_id=2
## method: POST,
## query parameters: params,
- Request:-
```json
{
    "profile_id":2,
}
```
- Response:-
```json
{
    "message": "Profile Inactive.",
    "status": true
}
```
# 9. make photo visible API: http://127.0.0.1:8000/api/profiles/VerifiedPhotoVisiblity/?profile_id=3
## Method: POST,
## Query parameters: params
- Request:-
```json
{
    "profile_id":3,
}
``` 
- Response:-
```json
{
    "message": "profile visiblity verified successfully.",
    "status": {
        "id": 3,
        "profile_id": "MAT000003",
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
        "profile_photo": null,
        "is_profile_completed": false,
        "profile_status": "NEW",
        "is_photo_visible": true,
        "is_verified": true,
        "is_active": true,
        "created_at": "2026-08-06T06:07:27.871230Z",
        "updated_at": "2026-08-08T09:39:57.793849Z",
        "user": 6,
        "denomination": 1
    }
}
```

# 10. multi parameter profile filter API: http://127.0.0.1:8000/api/profiles/searchProfiles/?gender=MALE&profile_type=GROOM

## Method: GET
## Query Parameters: Params
- Request:-
```json
{
    1.
    "gender":"MALE",
    "profile_type":"GROOM"

    2.,
    "gender":"MALE",
    "profile_type":"GROOM",
    "height":"5.2",
    "weight":"70",
    "marital_status":"UNMARRIED"
}
```
- Response:-

```json
{
    "message": "Profiles retrieved successfully.",
    "data": [
        {
            "id": 3,
            "profile_id": "MAT000003",
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
            "profile_photo": null,
            "is_profile_completed": false,
            "profile_status": "NEW",
            "is_photo_visible": true,
            "is_verified": true,
            "is_active": true,
            "created_at": "2026-08-06T06:07:27.871230Z",
            "updated_at": "2026-08-08T09:39:57.793849Z",
            "user": 6,
            "denomination": 1
        }
    ],
    {
    "message": "Profiles retrieved successfully.",
    "data": [
        {
            "id": 3,
            "profile_id": "MAT000003",
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
            "profile_photo": null,
            "is_profile_completed": false,
            "profile_status": "NEW",
            "is_photo_visible": true,
            "is_verified": true,
            "is_active": true,
            "created_at": "2026-08-06T06:07:27.871230Z",
            "updated_at": "2026-08-08T09:39:57.793849Z",
            "user": 6,
            "denomination": 1
        }
    ]
}
}
```

# 11. photo update API: http://127.0.0.1:8000/api/profiles/UpdatePhoto/4/
## Method: PUT,
## Query Parameters: from-data
- Request:-
```json
{
    "profile_photo":
}
```
- Response:-
```json
{
    "message": "Profile photo updated successfully.",
    "data": {
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
        "profile_status": "NEW",
        "is_photo_visible": true,
        "is_verified": false,
        "is_active": true,
        "created_at": "2026-08-08T07:02:30.995540Z",
        "updated_at": "2026-08-08T11:33:12.528754Z",
        "user": 7,
        "denomination": 1
    }
}
```
# 12. Approved profile API: http://127.0.0.1:8000/api/profiles/RejectProfile/?profile_id=3

## Method: patch
## Query Parameters: Params
- Request:-
```json
{
    "profile_id":4,
}
```
- Response:-
```json
{
    "message": "Profile approved successfully.",
    "data": {
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
        "is_photo_visible": false,
        "is_verified": true,
        "is_active": true,
        "created_at": "2026-08-08T07:02:30.995540Z",
        "updated_at": "2026-08-08T12:05:53.094783Z",
        "user": 7,
        "denomination": 1
    }
}
```

# 13. Reject Profile API: http://127.0.0.1:8000/api/profiles/RejectProfile/?profile_id=3
## Method: Patch
## Query Parameters: Params
- Request:-
```json
{
    "profile_id":3,
}
```
- Response:-
```json
{
    "message": "Profile rejected successfully.",
    "data": {
        "id": 3,
        "profile_id": "MAT000003",
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
        "profile_photo": null,
        "is_profile_completed": false,
        "profile_status": "REJECTED",
        "is_photo_visible": false,
        "is_verified": false,
        "is_active": true,
        "created_at": "2026-08-06T06:07:27.871230Z",
        "updated_at": "2026-08-08T12:14:27.669158Z",
        "user": 6,
        "denomination": 1
    }
}
```

