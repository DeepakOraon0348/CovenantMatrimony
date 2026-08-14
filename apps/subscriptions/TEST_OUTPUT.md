# 1. create plane API: http://127.0.0.1:8000/api/subscriptions/CreatePlan/
## Methods: POST, 
## Query Parameters: JSON
- Request:-
```json
{
    "name": "GOLD",
    "price": 999.00,
    "duration_days": 30,
    "max_matches_per_day": 20,
    "featured_profiles": true,
    "priority_support": true,
    "is_active": true
},
{
    "name": "SILVER",
    "price": 499.00,
    "duration_days": 30,
    "max_matches_per_day": 10,
    "featured_profiles": true,
    "priority_support": true,
    "is_active": true
},
{
    "name": "DIAMOND",
    "price": 1499.00,
    "duration_days": 30,
    "max_matches_per_day": 30,
    "featured_profiles": true,
    "priority_support": true,
    "is_active": true
},
{
    "name": "FREE",
    "price": 0.00,
    "duration_days": 5,
    "max_matches_per_day": 1,
    "featured_profiles": true,
    "priority_support": true,
    "is_active": true
}
```
- Response
```json
{
    "success": true,
    "message": "Subscription plan created successfully.",
    "data": {
        "id": 1,
        "name": "GOLD",
        "price": "999.00",
        "duration_days": 30,
        "max_matches_per_day": 20,
        "featured_profiles": true,
        "priority_support": true,
        "is_active": true,
        "created_at": "2026-08-11T07:10:26.071470Z",
        "updated_at": "2026-08-11T07:10:26.071499Z"
    }
},
{
    "success": true,
    "message": "Subscription plan created successfully.",
    "data": {
        "id": 2,
        "name": "SILVER",
        "price": "499.00",
        "duration_days": 30,
        "max_matches_per_day": 10,
        "featured_profiles": true,
        "priority_support": true,
        "is_active": true,
        "created_at": "2026-08-11T07:18:18.421959Z",
        "updated_at": "2026-08-11T07:18:18.421979Z"
    }
},
{
    "success": true,
    "message": "Subscription plan created successfully.",
    "data": {
        "id": 3,
        "name": "DIAMOND",
        "price": "1499.00",
        "duration_days": 30,
        "max_matches_per_day": 30,
        "featured_profiles": true,
        "priority_support": true,
        "is_active": true,
        "created_at": "2026-08-11T07:20:12.548274Z",
        "updated_at": "2026-08-11T07:20:12.548297Z"
    }
},
{
    "success": true,
    "message": "Subscription plan created successfully.",
    "data": {
        "id": 4,
        "name": "FREE",
        "price": "0.00",
        "duration_days": 5,
        "max_matches_per_day": 1,
        "featured_profiles": true,
        "priority_support": true,
        "is_active": true,
        "created_at": "2026-08-11T07:22:27.957078Z",
        "updated_at": "2026-08-11T07:22:27.957101Z"
    }
}
```

# 2. get all plane  API: http://127.0.0.1:8000/api/subscriptions/GetAllPlans/
## Method: Get
## Query Parameters: no 
- Response:-
```json
{
    "success": true,
    "message": "Subscription plans fetched successfully.",
    "total": 4,
    "data": [
        {
            "id": 4,
            "name": "FREE",
            "price": "0.00",
            "duration_days": 5,
            "max_matches_per_day": 1,
            "featured_profiles": true,
            "priority_support": true,
            "is_active": true,
            "created_at": "2026-08-11T07:22:27.957078Z",
            "updated_at": "2026-08-11T07:22:27.957101Z"
        },
        {
            "id": 2,
            "name": "SILVER",
            "price": "499.00",
            "duration_days": 30,
            "max_matches_per_day": 10,
            "featured_profiles": true,
            "priority_support": true,
            "is_active": true,
            "created_at": "2026-08-11T07:18:18.421959Z",
            "updated_at": "2026-08-11T07:18:18.421979Z"
        },
        {
            "id": 1,
            "name": "GOLD",
            "price": "999.00",
            "duration_days": 30,
            "max_matches_per_day": 20,
            "featured_profiles": true,
            "priority_support": true,
            "is_active": true,
            "created_at": "2026-08-11T07:10:26.071470Z",
            "updated_at": "2026-08-11T07:10:26.071499Z"
        },
        {
            "id": 3,
            "name": "DIAMOND",
            "price": "1499.00",
            "duration_days": 30,
            "max_matches_per_day": 30,
            "featured_profiles": true,
            "priority_support": true,
            "is_active": true,
            "created_at": "2026-08-11T07:20:12.548274Z",
            "updated_at": "2026-08-11T07:20:12.548297Z"
        }
    ]
}
```
# 3. get plan by id API: http://127.0.0.1:8000/api/subscriptions/GetPlan/?plane_id=2
## Method:GET
## Query Parameters: params
- Request:-
```json
{
    "plane_id":2,
}
```

- Response:-
```json
{
    "success": true,
    "message": "Subscription plan fetched successfully.",
    "data": {
        "id": 2,
        "name": "SILVER",
        "price": "499.00",
        "duration_days": 30,
        "max_matches_per_day": 10,
        "featured_profiles": true,
        "priority_support": true,
        "is_active": true,
        "created_at": "2026-08-11T07:18:18.421959Z",
        "updated_at": "2026-08-11T07:18:18.421979Z"
    }
}
```
# 4. Update Plan API:http://127.0.0.1:8000/api/subscriptions/UpdatePlan/2/
## Method: PUT,
## Query Parameters: JSON,
- Request:-
```json
{
    "name": "SILVER",
    "price": 699.00,
    "duration_days": 30,
    "max_matches_per_day": 10,
    "featured_profiles": true,
    "priority_support": true,
    "is_active": true
}
```
- Response:-
```json
{
    "success": true,
    "message": "Subscription plan updated successfully.",
    "data": {
        "id": 2,
        "name": "SILVER",
        "price": "699.00",
        "duration_days": 30,
        "max_matches_per_day": 10,
        "featured_profiles": true,
        "priority_support": true,
        "is_active": true,
        "created_at": "2026-08-11T07:18:18.421959Z",
        "updated_at": "2026-08-11T08:08:24.396079Z"
    }
}
```
# 5. Delete Plan API: http://127.0.0.1:8000/api/subscriptions/DeletePlan/?plane_id=4
## Methods: DELETE
## Query-Parameters: params
- Request:-
```json
{
    "plane_id":4,
}
```
- Response:-
```json
{
    "success": true,
    "message": "Subscription plan deleted successfully."
}
```