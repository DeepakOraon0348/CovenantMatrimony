# 1. Create Prayers API: http://127.0.0.1:8000/api/prayers/CreatePrayer/
## METHOD:POST
## Query Parameters: json
- Request:-
```json
{
    "church": 1,
    "title": "Prayer for Church Members",
    "note": "Please pray for the health, peace and spiritual growth of all church members."
}
```
- Response:-
```json
{
    "message": "Prayer created successfully.",
    "data": {
        "id": 1,
        "church": 1,
        "church_name": "St. Peter Church",
        "created_by": 12,
        "created_by_name": "Rita Kumari",
        "title": "Prayer for Church Members",
        "note": "Please pray for the health, peace and spiritual growth of all church members.",
        "status": "ONGOING",
        "created_at": "2026-08-13T11:11:54.622396Z",
        "completed_at": null,
        "updated_at": "2026-08-13T11:11:54.622505Z"
    }
}
```
# 2. Get all Prayers api: http://127.0.0.1:8000/api/prayers/GetAllPrayer/
## METHOD:post,
## Query parameters: login Required
- Respose:-
```json
{
    "message": "All prayers retrieved successfully.",
    "total": 1,
    "data": [
        {
            "id": 1,
            "church": 1,
            "church_name": "St. Peter Church",
            "created_by": 12,
            "created_by_name": "Rita Kumari",
            "title": "Prayer for Church Members",
            "note": "Please pray for the health, peace and spiritual growth of all church members.",
            "status": "ONGOING",
            "created_at": "2026-08-13T11:11:54.622396Z",
            "completed_at": null,
            "updated_at": "2026-08-13T11:11:54.622505Z"
        }
    ]
}
```
# 3. GET my Church prayer API: http://127.0.0.1:8000/api/prayers/GetMyChurchPrayer/
## Methods: get
## Query parameters: login Required
- Response:-
```json
{
    "message": "Church prayers retrieved successfully.",
    "total": 1,
    "data": [
        {
            "id": 1,
            "church": 1,
            "church_name": "St. Peter Church",
            "created_by": 12,
            "created_by_name": "Rita Kumari",
            "title": "Prayer for Church Members",
            "note": "Please pray for the health, peace and spiritual growth of all church members.",
            "status": "ONGOING",
            "created_at": "2026-08-13T11:11:54.622396Z",
            "completed_at": null,
            "updated_at": "2026-08-13T11:11:54.622505Z"
        }
    ]
}
```
# 4. Get prayer by id API: http://127.0.0.1:8000/api/prayers/GetPrayer/?prayer_id=1
## METHOD: GET
## QUERY PARAMETERS:PARAMS
- Request:-
```json
{
    "prayer_id":1,
}
```
- Response:-
```json
{
    "message": "Prayer retrieved successfully.",
    "data": {
        "id": 1,
        "church": 1,
        "church_name": "St. Peter Church",
        "created_by": 12,
        "created_by_name": "Rita Kumari",
        "title": "Prayer for Church Members",
        "note": "Please pray for the health, peace and spiritual growth of all church members.",
        "status": "ONGOING",
        "created_at": "2026-08-13T11:11:54.622396Z",
        "completed_at": null,
        "updated_at": "2026-08-13T11:11:54.622505Z"
    }
}
```
# 5. Update Prayer API: http://127.0.0.1:8000/api/prayers/UpdatePrayer/?prayer_id=1
## Method:patch
## Query parameters: prayer_id in params and update data in json body.
- Request:-
```json
{
    "prayer_id":1,
},
{
    "church": 1,
    "title": "Prayer for Church Members123456",
    "note": "Please pray for the health, peace and spiritual growth of all church members."
}
```
- Response:-
```json
{
    "message": "Prayer updated successfully.",
    "data": {
        "id": 1,
        "church": 1,
        "church_name": "St. Peter Church",
        "created_by": 12,
        "created_by_name": "Rita Kumari",
        "title": "Prayer for Church Members123456",
        "note": "Please pray for the health, peace and spiritual growth of all church members.",
        "status": "ONGOING",
        "created_at": "2026-08-13T11:11:54.622396Z",
        "completed_at": null,
        "updated_at": "2026-08-13T11:33:47.604055Z"
    }
}
```
# 6. prayer status update API: http://127.0.0.1:8000/api/prayers/UpdatePrayerStatus/?prayer_id=1
## Method: patch
## Query parameters: prayer_id in params and status update data in json 
- Request:-
```json
{
    "prayer_id":1,
},
{
    "status":"COMPLETED"
}
```
- Response:-
```json
{
    "message": "Prayer status updated successfully.",
    "data": {
        "id": 1,
        "church": 1,
        "church_name": "St. Peter Church",
        "created_by": 12,
        "created_by_name": "Rita Kumari",
        "title": "Prayer for Church Members123456",
        "note": "Please pray for the health, peace and spiritual growth of all church members.",
        "status": "COMPLETED",
        "created_at": "2026-08-13T11:11:54.622396Z",
        "completed_at": "2026-08-13T11:44:31.022364Z",
        "updated_at": "2026-08-13T11:44:31.022792Z"
    }
}
```
# 7. delete Prayer API: http://127.0.0.1:8000/api/prayers/DeletePrayer/?prayer_id=1
## METHOD: DELETE
## QUERY PARAMETERS: PARAMS
- Request:-
```json
{
    "prayer_id":1,
}
```
- Response:-
```json
{
    "message": "Prayer deleted successfully."
}
```