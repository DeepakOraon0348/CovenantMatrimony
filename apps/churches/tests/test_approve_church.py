from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.branches.models import Branch
from apps.churches.models import Church


class ApproveChurchTestCase(APITestCase):

    def setUp(self):
        self.branch = Branch.objects.create(
            name="Ranchi Branch",
            code="RAN001",
            email="ranchi@gmail.com",
            phone="9876543210",
            address="Ranchi",
            city="Ranchi",
            state="Jharkhand",
            country="India",
            pincode="834001",
        )

        self.church = Church.objects.create(
            branch=self.branch,
            name="St. Peter Church",
            code="STP001",
            pastor_name="Rev. John Lakra",
            email="church@gmail.com",
            phone="9876543210",
            address="Main Road",
            city="Ranchi",
            state="Jharkhand",
            country="India",
            pincode="834001",
        )

    def test_approve_church(self):  # ✅ Inside the class

        url = reverse("approve_church")

        response = self.client.post(f"{url}?church_id={self.church.id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.church.refresh_from_db()

        self.assertEqual(
            self.church.verification_status,
            Church.VerificationStatus.APPROVED,
        )
