import hmac
import hashlib

order_id = "order_TP7PSGyyyhVPyw"
payment_id = "rzp_test_TOkPEiyWgLMO0D"
key_secret = "YOUR_RAZORPAY_KEY_SECRET"

message = f"{order_id}|{payment_id}"

signature = hmac.new(
    key_secret.encode(),
    message.encode(),
    hashlib.sha256
).hexdigest()

print("Signature:")
print(signature)
