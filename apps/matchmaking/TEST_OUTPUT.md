# 1. create matching intrest: http://127.0.0.1:8000/api/matchmaking/CreateInterest/
## Method: POST
## Query-parameters: JSON
- Request:-
```json
{
    "receiver_profile": 2,
    "message": "I am interested in your profile."
},
{
    "receiver_profile": 3,
    "message": "I am interested in your profile."
}
```
- Response:- 
```json
{
    "message": "Interest request sent successfully.",
    "data": {
        "id": 1,
        "sender_profile": 4,
        "receiver_profile": 2,
        "status": "PENDING",
        "message": "I am interested in your profile.",
        "created_at": "2026-08-12T10:31:20.997180Z",
        "updated_at": "2026-08-12T10:31:20.999025Z"
    }
},
{
    "message": "Interest request sent successfully.",
    "data": {
        "id": 2,
        "sender_profile": 4,
        "receiver_profile": 3,
        "status": "PENDING",
        "message": "I am interested in your profile.",
        "created_at": "2026-08-12T10:35:20.535888Z",
        "updated_at": "2026-08-12T10:35:20.536572Z"
    }
}
```
# 2. get sent all intrest: http://127.0.0.1:8000/api/matchmaking/GetSentInterest/
## Method:GET
## Query-Parameters:no
- Response:-
```json
{
    "message": "Sent interest requests fetched successfully.",
    "data": [
        {
            "id": 2,
            "sender_profile": 4,
            "receiver_profile": 3,
            "status": "PENDING",
            "message": "I am interested in your profile.",
            "created_at": "2026-08-12T10:35:20.535888Z",
            "updated_at": "2026-08-12T10:35:20.536572Z"
        },
        {
            "id": 1,
            "sender_profile": 4,
            "receiver_profile": 2,
            "status": "PENDING",
            "message": "I am interested in your profile.",
            "created_at": "2026-08-12T10:31:20.997180Z",
            "updated_at": "2026-08-12T10:31:20.999025Z"
        }
    ],
    "total": 2
}
```
# 3. Get Received Interest API: http://127.0.0.1:8000/api/matchmaking/GetReceivedInterest/
## Method: GET
## Query-Parameters: no
- Response:-
```json
{
    "message": "Received interest requests fetched successfully.",
    "data": [
        {
            "id": 3,
            "sender_profile": 6,
            "receiver_profile": 4,
            "status": "PENDING",
            "message": "I am interested in your profile.",
            "created_at": "2026-08-12T10:55:53.251008Z",
            "updated_at": "2026-08-12T10:55:53.251201Z"
        }
    ],
    "total": 1
}
```
# 4. get interest by id API: http://127.0.0.1:8000/api/matchmaking/GetInterest/?interest_id=3
## Method: Get
## Query-parameters: params,
- Response:-
```json
{
    "message": "Interest request fetched successfully.",
    "data": {
        "id": 3,
        "sender_profile": 6,
        "receiver_profile": 4,
        "status": "PENDING",
        "message": "I am interested in your profile.",
        "created_at": "2026-08-12T10:55:53.251008Z",
        "updated_at": "2026-08-12T10:55:53.251201Z"
    }
}
```
# 5. Accept Intrest API: http://127.0.0.1:8000/api/matchmaking/AcceptInterest/?interest_id=3
## Methods: Post
## Query-Parameters: params
- Request:-
```json
{
    "interest_id":3,
}
```
- Response:-
```json
{
    "message": "Interest request accepted and match created successfully.",
    "data": {
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
        "status": "ACTIVE",
        "matched_at": "2026-08-12T12:18:57.928217Z",
        "updated_at": "2026-08-12T12:18:57.928275Z"
    }
}
```
# 6. Reject Interest API: http://127.0.0.1:8000/api/matchmaking/RejectInterest/?intrest_id=4
## Methods: Post
## Qurey parameters: Params
- Request:-
```json
{
    "intrest_id":4,
}
```
- Response:-
```json
{
    "message": "Interest request rejected successfully.",
    "data": {
        "id": 4,
        "sender_profile": 7,
        "receiver_profile": 4,
        "status": "REJECTED",
        "message": "I am interested in your profile.",
        "created_at": "2026-08-12T12:33:36.751587Z",
        "updated_at": "2026-08-12T17:54:44.348081Z"
    }
}
```
# 7. interest Request cancel API: http://127.0.0.1:8000/api/matchmaking/CancelInterest/?interest_id=1
## METHOD: POST
## Query Parameters: params
- Request:-
```json
{
    "interest_id":1,
}
```
- Response:-
```json
{
    "message": "Interest request cancelled successfully.",
    "data": {
        "id": 1,
        "sender_profile": 4,
        "receiver_profile": 2,
        "status": "REJECTED",
        "message": "I am interested in your profile.",
        "created_at": "2026-08-12T10:31:20.997180Z",
        "updated_at": "2026-08-12T18:22:36.330268Z"
    }
}
```
# 8. Get my matches API: http://127.0.0.1:8000/api/matchmaking/GetMyMatches/

## Method: Get
## Query Parameters: no only user login required.
- Response:-
```json
{
    "message": "Matches fetched successfully.",
    "data": [
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
            "status": "ACTIVE",
            "matched_at": "2026-08-12T12:18:57.928217Z",
            "updated_at": "2026-08-12T12:18:57.928275Z"
        }
    ],
    "total": 1
}
```
# 9. get the match by  id API:http://127.0.0.1:8000/api/matchmaking/GetMatch/?match_id=1
## METHOD:GET
## QUERY PARAMETERS:PARAMS
- Request:- 
```json
{
    "match_id":1,
}
```
- Response:-
```json
{
    "message": "Match fetched successfully.",
    "data": {
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
        "status": "ACTIVE",
        "matched_at": "2026-08-12T12:18:57.928217Z",
        "updated_at": "2026-08-12T12:18:57.928275Z"
    }
}
```
# 10. Close the match API: http://127.0.0.1:8000/api/matchmaking/CloseMatch/?match_id=1
## METHOD: POST
## QUERY PARAMETERS: PARAMS
- Request:-
```json
{
    "match_id":1
}
```
- Response:-
```json
{
    "message": "Match closed successfully.",
    "data": {
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
    }
}
```