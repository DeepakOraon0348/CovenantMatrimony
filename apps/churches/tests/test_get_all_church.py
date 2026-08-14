from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class GetAllChurchesTestCase(APITestCase):

    def test_get_all_churches(self):

        url = reverse("get_all_churches")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
