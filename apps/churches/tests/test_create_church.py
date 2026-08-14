from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from apps.branches.models import Branch


class CreateChurchTestCase(APITestCase):

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

    def test_create_church(self):
        url = reverse("create_church")

        payload = {
            "branch": self.branch.id,
            "name": "St. Peter Church",
            "code": "STP001",
            "pastor_name": "Rev. John Lakra",
            "email": "church@gmail.com",
            "phone": "9876543210",
            "address": "Main Road",
            "city": "Ranchi",
            "state": "Jharkhand",
            "country": "India",
            "pincode": "834001",
        }

        response = self.client.post(url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
