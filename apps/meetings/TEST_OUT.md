# 1. create all Meeting API: http://127.0.0.1:8000/api/meetings/CreateMeeting/
## Method: POST,
## Query Parameters: JSON
- Request:-
```json
{
    "match": 2,
    "meeting_date": "2026-08-20",
    "meeting_time": "18:30:00",
    "venue": "St. Mary's Church, Ranchi",
    "remarks": "First meeting between both families."
}
```
- Response:-
```json
{
    "message": "Meeting scheduled successfully.",
    "data": {
        "id": 1,
        "match": 2,
        "meeting_date": "2026-08-20",
        "meeting_time": "18:30:00",
        "venue": "St. Mary's Church, Ranchi",
        "status": "SCHEDULED",
        "remarks": "First meeting between both families.",
        "created_at": "2026-08-13T07:30:49.796373Z",
        "updated_at": "2026-08-13T07:30:49.796411Z"
    }
}
```
# 2. Get all meeting API: http://127.0.0.1:8000/api/meetings/GetAllMeeting/
## Methods: Get,
## Query-parameters: only access jwt token
- Response:- 
```json
{
    "message": "All meetings retrieved successfully.",
    "total": 1,
    "data": [
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
        }
    ]
}
```
# 3. Get My Meeting(user) API: http://127.0.0.1:8000/api/meetings/GetMyMeetings/
## Method: GET,
## Query-parameters: user login required,
- Response:-
```json
{
    "message": "Meetings fetched successfully.",
    "total": 2,
    "data": [
        {
            "id": 2,
            "match": 3,
            "meeting_date": "2026-08-22",
            "meeting_time": "18:30:00",
            "venue": "St. Mary's Church, Ranchi",
            "status": "SCHEDULED",
            "remarks": "First meeting between both families.",
            "created_at": "2026-08-13T08:07:16.665308Z",
            "updated_at": "2026-08-13T08:07:16.665324Z"
        },
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
        }
    ]
}
```
# 4. Get Meeting by id API:http://127.0.0.1:8000/api/meetings/GetMeeting/?meeting_id=1
## Methods: get
## Query-parameters: params

- Request:-
```json
{
    "meeting_id":1,
}
```
- Request:-
```json
{
    "message": "Meeting fetched successfully.",
    "data": {
        "id": 1,
        "match": 2,
        "meeting_date": "2026-08-20",
        "meeting_time": "18:30:00",
        "venue": "St. Mary's Church, Ranchi",
        "status": "SCHEDULED",
        "remarks": "First meeting between both families.",
        "created_at": "2026-08-13T07:30:49.796373Z",
        "updated_at": "2026-08-13T07:30:49.796411Z"
    }
}
```
# 5. update meeting API: http://127.0.0.1:8000/api/meetings/UpdateMeeting/?meeting_id=2
## Methods:PUT
## Query parameters: params (meeting_id) and json update data
- Request:-
```json
{
   "meeting_id":2,
},
{
    "match": 3,
    "meeting_date": "2026-08-30",
    "meeting_time": "18:30:00",
    "venue": "St. Mary's Church, Ranchi",
    "remarks": "First meeting between both families."
}
```
- Response:-
```json
{
    "message": "Meeting updated successfully.",
    "data": {
        "id": 2,
        "match": 3,
        "meeting_date": "2026-08-30",
        "meeting_time": "18:30:00",
        "venue": "St. Mary's Church, Ranchi",
        "status": "SCHEDULED",
        "remarks": "First meeting between both families.",
        "created_at": "2026-08-13T08:07:16.665308Z",
        "updated_at": "2026-08-13T08:22:32.242932Z"
    }
}
```
# 6. Cancel Meeting API: http://127.0.0.1:8000/api/meetings/CancelMeeting/?meeting_id=2
## Method: POST
## Query-Parameters: params
- Request:-
```json
{
    "meeting_id":2,
}
```
- Response:-
```json
{
    "message": "Meeting cancelled successfully.",
    "data": {
        "id": 2,
        "match": 3,
        "meeting_date": "2026-08-30",
        "meeting_time": "18:30:00",
        "venue": "St. Mary's Church, Ranchi",
        "status": "CANCELLED",
        "remarks": "First meeting between both families.",
        "created_at": "2026-08-13T08:07:16.665308Z",
        "updated_at": "2026-08-13T08:28:22.319985Z"
    }
}
```
# 7. meeting complete API:http://127.0.0.1:8000/api/meetings/MeetingComplete/?meeting_id=3
## Method: POST
## Query Parameters: params
- Request:- 
```json
{
    "meeting_id":3,
}
```
- Response:-
```json
{
    "message": "Meeting status Update successfully.",
    "data": {
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
}
```