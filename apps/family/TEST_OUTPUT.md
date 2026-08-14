# 1. create family API: http://127.0.0.1:8000/api/family/CreateFamily/4/
## Methods: POST
## Query Parameters: JSON 
- Request:-
```json
{
    "father_name": "Ramesh Oraon",
    "mother_name": "Sunita Oraon",
    "father_occupation": "Government Employee",
    "mother_occupation": "Teacher",
    "brothers": 1,
    "sisters": 2,
    "family_type": "NUCLEAR"
}

```
- Response:-
```json
{
    "message": "Family details created successfully.",
    "data": {
        "id": 1,
        "father_name": "Ramesh Oraon",
        "mother_name": "Sunita Oraon",
        "father_occupation": "Government Employee",
        "mother_occupation": "Teacher",
        "brothers": 1,
        "sisters": 2,
        "family_type": "NUCLEAR",
        "created_at": "2026-08-10T06:11:01.796837Z",
        "updated_at": "2026-08-10T06:11:01.796901Z",
        "profile": 4
    }
}
```
# 2. Get My Family API: http://127.0.0.1:8000/api/family/GetMyFamily/?profile_id=4
## Method: GET
## Query-parameters: params

- Request:-
```json
{
    "profile_id":4,
}
```
- Response:-
```json
{
    "message": "Family details fetched successfully.",
    "data": {
        "id": 1,
        "father_name": "Ramesh Oraon",
        "mother_name": "Sunita Oraon",
        "father_occupation": "Government Employee",
        "mother_occupation": "Teacher",
        "brothers": 1,
        "sisters": 2,
        "family_type": "NUCLEAR",
        "created_at": "2026-08-10T06:11:01.796837Z",
        "updated_at": "2026-08-10T06:11:01.796901Z",
        "profile": 4
    }
}
```
# 3.Update family API:http://127.0.0.1:8000/api/family/UpdateFamily/4/
## Method: PUT
## Query parameters: josn
- Request:-
```json
{
    "father_name": "Ramesh Oraon",
    "mother_name": "Sunita Oraon",
    "father_occupation": "Government Employee",
    "mother_occupation": "Railway job",
    "brothers": 1,
    "sisters": 2,
    "family_type": "NUCLEAR"
}
```
- Reponse:-
```json
{
    "message": "Family details updated successfully.",
    "data": {
        "id": 1,
        "father_name": "Ramesh Oraon",
        "mother_name": "Sunita Oraon",
        "father_occupation": "Government Employee",
        "mother_occupation": "Railway job",
        "brothers": 1,
        "sisters": 2,
        "family_type": "NUCLEAR",
        "created_at": "2026-08-10T06:11:01.796837Z",
        "updated_at": "2026-08-10T06:43:05.123610Z",
        "profile": 4
    }
}
```
# 4. Deletes family API: http://127.0.0.1:8000/api/family/DeleteFamily/?profile_id=4
## Method: Delete
## Query parameters: params
- Request:-
```json
{
    "profile_id":4,
}
```
