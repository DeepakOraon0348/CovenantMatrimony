# 1. Create subscription API: http://127.0.0.1:8000/api/user_subscriptions/CreateSubscription/
## Method:POST
## Query-Parameters: form-data
- Request:-
```json
{
    "plan":2,
    "user_id":7
}
``` 
- Response:- 
```json
{
    "message": "Subscription created successfully.",
    "data": {
        "id": 2,
        "plan": 2,
        "start_date": "2026-08-11T10:33:52.963047Z",
        "expiry_date": "2026-09-10T10:33:52.963047Z",
        "is_active": true,
        "created_at": "2026-08-11T10:33:52.963379Z",
        "updated_at": "2026-08-11T10:33:52.963388Z",
        "user": 7
    }
}
```

# 2. get my subscription API: http://127.0.0.1:8000/api/user_subscriptions/GetMySubscription/
## Method: GET
## Query Parameters: no
- Response:-
```json
{
    "message": "Subscription fetched successfully.",
    "data": {
        "id": 1,
        "plan": 2,
        "start_date": "2026-08-11T10:03:19.220959Z",
        "expiry_date": "2026-09-10T10:03:19.220959Z",
        "is_active": true,
        "created_at": "2026-08-11T10:03:19.225372Z",
        "updated_at": "2026-08-11T10:03:19.225380Z",
        "user": 7
    }
}
```
# 3. get subscription by id API: http://127.0.0.1:8000/api/user_subscriptions/GetSubscriptionById/?subscription_id=2
## Method: get
## Query-Parameters:params
- Request:-
```json
{
    "subscription_id":2,
}
```
- Response:-
```json
{
    "message": "Subscription fetched successfully.",
    "data": {
        "id": 2,
        "plan": 2,
        "start_date": "2026-08-11T10:33:52.963047Z",
        "expiry_date": "2026-09-10T10:33:52.963047Z",
        "is_active": true,
        "created_at": "2026-08-11T10:33:52.963379Z",
        "updated_at": "2026-08-11T10:33:52.963388Z",
        "user": 7
    }
}
```
# 4. Cancel Subscription API: http://127.0.0.1:8000/api/user_subscriptions/CancelSubscription/?subscription_id=2

## Method: PATCH
## Query-Parameters: params,
- Request:- 
```json
{
    "subscription_id":2,
}
```
- Respose:-
```json
{
    "message": "Subscription cancelled successfully.",
    "data": {
        "id": 2,
        "plan": 2,
        "start_date": "2026-08-11T10:33:52.963047Z",
        "expiry_date": "2026-09-10T10:33:52.963047Z",
        "is_active": false,
        "created_at": "2026-08-11T10:33:52.963379Z",
        "updated_at": "2026-08-11T11:35:24.536701Z",
        "user": 7
    }
}
```