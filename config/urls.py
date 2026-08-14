"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from .views import razorpay_test

urlpatterns = [
    path("admin/", admin.site.urls),
     path(
        "razorpay-test/",
        razorpay_test,
        name="razorpay-test",
    ),
    path(
        "api/payments/",
        include("apps.payments.urls"),
    ),
    path("api/auth/", include("apps.accounts.urls")),
    path("api/branch/", include("apps.branches.urls")),
    path("api/churches/", include("apps.churches.urls")),
    path("api/common/", include("apps.common.urls")),
    path("api/dashboard/", include("apps.dashboard.urls")),
    path("api/matchmaking/", include("apps.matchmaking.urls")),
    path("api/meetings/", include("apps.meetings.urls")),
    path("api/notificatoins/", include("apps.notifications.urls")),
    path("api/payments/", include("apps.payments.urls")),
    path("api/profiles/", include("apps.profiles.urls")),
    path("api/reports/", include("apps.reports.urls")),
    path("api/subscriptions/", include("apps.subscriptions.urls")),
    path("api/family/", include("apps.family.urls")),
    path("api/documents/", include("apps.documents.urls")),
    path("api/user_subscriptions/", include("apps.user_subscriptions.urls")),
    path("api/marriages/", include("apps.marriages.urls")),
    path("api/prayers/", include("apps.prayers.urls"))
]
