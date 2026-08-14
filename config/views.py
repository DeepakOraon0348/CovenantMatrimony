from django.shortcuts import render


def razorpay_test(request):
    return render(
        request,
        "razorpay_test.html"
    )