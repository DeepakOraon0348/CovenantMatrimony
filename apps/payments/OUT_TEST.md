# 1. create order API: http://127.0.0.1:8000/api/payments/CreatePayment/
## Methods: POST
## Query Parameters:form-data
- Request:-
```json
{
    "plan_id":1,
}
```
- Response:-
```json
{
    "message": "Razorpay order created successfully.",
    "data": {
        "payment_id": 1,
        "razorpay_key_id": "rzp_test_TOkPEiyWgLMO0D",
        "razorpay_order_id": "order_TOlVrVtLkhKAZw",
        "amount": 99900,
        "currency": "INR",
        "plan": "GOLD"
    }
}
```

# 2. verify payment API:http://127.0.0.1:8000/api/payments/VerifyPayment/
## Methods: POST
## Query-Parameters: JOSN
- Request:-
```json
{
"razorpay_payment_id": "pay_TP92PF1N1DX1Aw",
"razorpay_order_id": "order_TP92AkQpwQvD2k",
"razorpay_signature": "8c32fa2db465e4b6ca44cbd96f48e31f652a10fd1a34d2c26a1da473d523dae4"
}
```
- Response:-
```json
 {
    "message": "Payment verified successfully.",
    "data": {
        "id": 4,
        "amount": "699.00",
        "payment_method": "RAZORPAY",
        "transaction_id": "pay_TP92PF1N1DX1Aw",
        "razorpay_order_id": "order_TP92AkQpwQvD2k",
        "razorpay_payment_id": "pay_TP92PF1N1DX1Aw",
        "razorpay_signature": "8c32fa2db465e4b6ca44cbd96f48e31f652a10fd1a34d2c26a1da473d523dae4",
        "payment_status": "SUCCESS",
        "paid_at": "2026-08-13T05:51:02.025053Z",
        "created_at": "2026-08-13T05:50:32.442401Z",
        "updated_at": "2026-08-13T05:51:02.061644Z",
        "user": 7,
        "plan": 2,
        "user_subscription": 3
    }
}
```

# 3. Get My Payment Details API: http://127.0.0.1:8000/api/payments/GetMyPayments/
## Methods: GET,
## Query-parameters: only required JWT access it from session storage.
- Response:-
```json
{
    "message": "Payments fetched successfully.",
    "data": [
        {
            "id": 4,
            "amount": "699.00",
            "payment_method": "RAZORPAY",
            "transaction_id": "pay_TP92PF1N1DX1Aw",
            "razorpay_order_id": "order_TP92AkQpwQvD2k",
            "razorpay_payment_id": "pay_TP92PF1N1DX1Aw",
            "razorpay_signature": "8c32fa2db465e4b6ca44cbd96f48e31f652a10fd1a34d2c26a1da473d523dae4",
            "payment_status": "SUCCESS",
            "paid_at": "2026-08-13T05:51:02.025053Z",
            "created_at": "2026-08-13T05:50:32.442401Z",
            "updated_at": "2026-08-13T05:51:02.061644Z",
            "user": 7,
            "plan": 2,
            "user_subscription": 3
        },
        {
            "id": 3,
            "amount": "999.00",
            "payment_method": "RAZORPAY",
            "transaction_id": null,
            "razorpay_order_id": "order_TP7PSGyyyhVPyw",
            "razorpay_payment_id": null,
            "razorpay_signature": null,
            "payment_status": "PENDING",
            "paid_at": null,
            "created_at": "2026-08-13T04:15:11.664932Z",
            "updated_at": "2026-08-13T04:15:11.665829Z",
            "user": 7,
            "plan": 1,
            "user_subscription": null
        },
        {
            "id": 2,
            "amount": "999.00",
            "payment_method": "RAZORPAY",
            "transaction_id": null,
            "razorpay_order_id": "order_TOm6wrSH50KVeJ",
            "razorpay_payment_id": null,
            "razorpay_signature": null,
            "payment_status": "PENDING",
            "paid_at": null,
            "created_at": "2026-08-12T07:25:04.703864Z",
            "updated_at": "2026-08-12T07:25:04.704484Z",
            "user": 7,
            "plan": 1,
            "user_subscription": null
        },
        {
            "id": 1,
            "amount": "999.00",
            "payment_method": "RAZORPAY",
            "transaction_id": null,
            "razorpay_order_id": "order_TOlVrVtLkhKAZw",
            "razorpay_payment_id": null,
            "razorpay_signature": null,
            "payment_status": "PENDING",
            "paid_at": null,
            "created_at": "2026-08-12T06:49:58.126567Z",
            "updated_at": "2026-08-12T06:49:58.126585Z",
            "user": 7,
            "plan": 1,
            "user_subscription": null
        }
    ]
}
```
# 4. Get Payment by id api: http://127.0.0.1:8000/api/payments/GetPayment/?payment_id=3
## Method:GET
## Query parameters:params
- Request:-
```json
{
    "payment_id"=3,
}
```
- Response:-
```json
{
    "message": "Payment fetched successfully.",
    "data": {
        "id": 3,
        "amount": "999.00",
        "payment_method": "RAZORPAY",
        "transaction_id": null,
        "razorpay_order_id": "order_TP7PSGyyyhVPyw",
        "razorpay_payment_id": null,
        "razorpay_signature": null,
        "payment_status": "PENDING",
        "paid_at": null,
        "created_at": "2026-08-13T04:15:11.664932Z",
        "updated_at": "2026-08-13T04:15:11.665829Z",
        "user": 7,
        "plan": 1,
        "user_subscription": null
    }
}
```