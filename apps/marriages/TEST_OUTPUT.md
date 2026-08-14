# 1. create merriage API: http://127.0.0.1:8000/api/marriages/CreateMarriage/
## METHODS: post
## Query-parameters: JSON
- Request:-
```json
{
    "meeting": 3,
    "marriage_date": "2026-09-15",
    "venue": "St. Mary's Church, Ranchi",
    "pastor_name": "Pastor John",
    "remarks": "Marriage ceremony scheduled successfully."
}
```
- Request:-
```json
{
    "message": "Marriage created successfully.",
    "data": {
        "id": 1,
        "meeting": 3,
        "marriage_date": "2026-09-15",
        "venue": "St. Mary's Church, Ranchi",
        "pastor_name": "Pastor John",
        "status": "PENDING",
        "remarks": "Marriage ceremony scheduled successfully.",
        "created_at": "2026-08-13T09:57:20.313112Z",
        "updated_at": "2026-08-13T09:57:20.313156Z"
    }
}
```
# 2. Get all Marriage API: http://127.0.0.1:8000/api/marriages/GetAllMarriage/
## Methods: get
## query-parameters: login Required
- Response:-
```json
{
    "message": "All marriages retrieved successfully.",
    "total": 1,
    "data": [
        {
            "id": 1,
            "meeting": 3,
            "marriage_date": "2026-09-15",
            "venue": "St. Mary's Church, Ranchi",
            "pastor_name": "Pastor John",
            "status": "PENDING",
            "remarks": "Marriage ceremony scheduled successfully.",
            "created_at": "2026-08-13T09:57:20.313112Z",
            "updated_at": "2026-08-13T09:57:20.313156Z"
        }
    ]
}
```
# 3. get my marriage Api: http://127.0.0.1:8000/api/marriages/GetMyMarriage/
## Methods:GET
## Query-Parameteres:user login required
- Response:-
```json
{
    "message": "My marriages retrieved successfully.",
    "total": 1,
    "data": [
        {
            "id": 1,
            "meeting": 3,
            "marriage_date": "2026-09-15",
            "venue": "St. Mary's Church, Ranchi",
            "pastor_name": "Pastor John",
            "status": "PENDING",
            "remarks": "Marriage ceremony scheduled successfully.",
            "created_at": "2026-08-13T09:57:20.313112Z",
            "updated_at": "2026-08-13T09:57:20.313156Z"
        }
    ]
}
```
# 4. Get Marriage BY ID API: http://127.0.0.1:8000/api/marriages/GetMarriage/?marriage_id=1
## Method: get
## Query Parameters: params
- Request:-
```json
{
    "marriage_id":1,
}
```
- Response:-
```json
{
    "message": "Marriage retrieved successfully.",
    "data": {
        "id": 1,
        "meeting": 3,
        "marriage_date": "2026-09-15",
        "venue": "St. Mary's Church, Ranchi",
        "pastor_name": "Pastor John",
        "status": "PENDING",
        "remarks": "Marriage ceremony scheduled successfully.",
        "created_at": "2026-08-13T09:57:20.313112Z",
        "updated_at": "2026-08-13T09:57:20.313156Z"
    }
}
```
# 5. Update Merriage API: http://127.0.0.1:8000/api/marriages/UpdateMarriage/1/
## Methods: put
## Query Parameters: JSON
- Request:-
```json
{
    "meeting": 3,
    "marriage_date": "2026-09-20",
    "venue": "St. Mary's Church, Ranchi",
    "pastor_name": "Pastor John",
    "remarks": "Marriage ceremony scheduled successfully."
}
```
- Response:-
```json
{
    "message": "Marriage updated successfully.",
    "data": {
        "id": 1,
        "meeting": 3,
        "marriage_date": "2026-09-20",
        "venue": "St. Mary's Church, Ranchi",
        "pastor_name": "Pastor John",
        "status": "PENDING",
        "remarks": "Marriage ceremony scheduled successfully.",
        "created_at": "2026-08-13T09:57:20.313112Z",
        "updated_at": "2026-08-13T10:30:31.365717Z"
    }
}
```
# 6. Update Marriage Status API: http://127.0.0.1:8000/api/marriages/UpdateMarriageStatus/?marriage_id=1
## Methods: patch
## query parameters:- marriage_id in params and stutus in json body.
- Request:-
```json
{
    "marriage_id":1,
},
{
    "status": "COMPLETED"
}
```
- Response:-
```json
{
    "message": "Marriage status updated successfully.",
    "data": {
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
}
```