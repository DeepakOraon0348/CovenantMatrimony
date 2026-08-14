# 1. create Denomination API:  http://127.0.0.1:8000/api/common/CreateDenomination/
## Method: POST
## Query Parameters: JSON
- Request:- 
```json
{
    "name": "Catholic",
    "description": "Roman Catholic denomination"
},
{
    "name": "Catholic",
    "description": "Duplicate"
}
```
- Response:-
```json
{
    "message": "Denomination created successfully.",
    "data": {
        "id": 1,
        "name": "Catholic",
        "description": "Roman Catholic denomination",
        "is_active": true,
        "created_at": "2026-08-05T10:44:46.405582Z"
    }
},
{
    "name": [
        "denomination already Exist"
    ]
}
```

# 2. Get All Denomination API: http://127.0.0.1:8000/api/common/GetAllDenomination/
## Method: Get
## Query Parameters: no
- Response:-
```json
{
    "message": "Get All Denomination List.",
    "tatal": 5,
    "data": [
        {
            "id": 1,
            "name": "Catholic",
            "description": "Roman Catholic denomination",
            "is_active": true,
            "created_at": "2026-08-05T10:44:46.405582Z"
        },
        {
            "id": 2,
            "name": "Protestant",
            "description": "Roman Protestant denomination",
            "is_active": true,
            "created_at": "2026-08-05T10:56:28.032006Z"
        },
        {
            "id": 3,
            "name": "Pentecostal",
            "description": "Roman Pentecostal denomination",
            "is_active": true,
            "created_at": "2026-08-05T10:57:04.157494Z"
        },
        {
            "id": 4,
            "name": "Baptist",
            "description": "Roman Baptist denomination",
            "is_active": true,
            "created_at": "2026-08-05T10:57:31.257101Z"
        },
        {
            "id": 5,
            "name": "Lutheran",
            "description": "Roman Baptist denomination",
            "is_active": true,
            "created_at": "2026-08-05T10:57:46.292505Z"
        }
    ]
}
```