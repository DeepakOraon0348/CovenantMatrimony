from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.branches.models import Branch
from apps.churches.models import Church


class SearchChurchTestCase(APITestCase):

    def setUp(self):

        branch = Branch.objects.create(
            name="Ranchi Branch",
            code="RAN001",
            email="branch@gmail.com",
            phone="9876543210",
            address="Main Road",
            city="Ranchi",
            state="Jharkhand",
            country="India",
            pincode="834001",
        )

        Church.objects.create(
            branch=branch,
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

    def test_search_by_city(self):

        url = reverse("search_churches")

        response = self.client.get(url, {"city": "Ranchi"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
