from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.branches.models import Branch
from apps.churches.models import Church


class UpdateChurchTestCase(APITestCase):

    def setUp(self):

        self.branch = Branch.objects.create(
            name="Ranchi Branch",
            code="RAN001",
            email="ranchi@gmail.com",
            phone="9876543210",
            address="Main Road",
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

    def test_update_church(self):

        url = reverse(
            "update_church",
            kwargs={"church_id": self.church.id},
        )

        payload = {
            "city": "Jamshedpur",
            "phone": "9123456789",
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.church.refresh_from_db()

        self.assertEqual(self.church.city, "Jamshedpur")
        self.assertEqual(self.church.phone, "9123456789")
