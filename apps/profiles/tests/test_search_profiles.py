from datetime import date

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.accounts.models import User
from apps.common.models import Denomination
from apps.profiles.models import Profile


class SearchProfilesTestCase(APITestCase):

    def setUp(self):

        self.denomination = Denomination.objects.create(name="Catholic")

        # Profile 1
        self.user1 = User.objects.create_user(
            email="female1@gmail.com",
            phone="9876543210",
            password="Deepak@123",
            first_name="Priya",
            last_name="Oraon",
        )

        self.profile1 = Profile.objects.create(
            user=self.user1,
            profile_id="MAT000001",
            profile_type="BRIDE",
            gender="FEMALE",
            date_of_birth=date(1999, 5, 10),
            denomination=self.denomination,
            marital_status="NEVER_MARRIED",
            height=5.6,
            weight=55,
            education="B.Tech",
            occupation="Software Engineer",
            annual_income=800000,
            about_me="Software engineer looking for a partner.",
            is_profile_completed=True,
            profile_status="VERIFIED",
            is_photo_visible=True,
            is_verified=True,
            is_active=True,
        )

        # Profile 2
        self.user2 = User.objects.create_user(
            email="female2@gmail.com",
            phone="9876543211",
            password="Deepak@123",
            first_name="Anita",
            last_name="Kujur",
        )

        self.profile2 = Profile.objects.create(
            user=self.user2,
            profile_id="MAT000002",
            profile_type="BRIDE",
            gender="FEMALE",
            date_of_birth=date(1997, 8, 15),
            denomination=self.denomination,
            marital_status="NEVER_MARRIED",
            height=5.9,
            weight=60,
            education="MBA",
            occupation="Teacher",
            annual_income=500000,
            about_me="Teacher looking for a partner.",
            is_profile_completed=True,
            profile_status="VERIFIED",
            is_photo_visible=True,
            is_verified=True,
            is_active=True,
        )

        # Profile 3 - Male
        self.user3 = User.objects.create_user(
            email="male1@gmail.com",
            phone="9876543212",
            password="Deepak@123",
            first_name="Rahul",
            last_name="Kumar",
        )

        self.profile3 = Profile.objects.create(
            user=self.user3,
            profile_id="MAT000003",
            profile_type="GROOM",
            gender="MALE",
            date_of_birth=date(1998, 2, 20),
            denomination=self.denomination,
            marital_status="NEVER_MARRIED",
            height=5.8,
            weight=70,
            education="B.Tech",
            occupation="Software Engineer",
            annual_income=900000,
            about_me="Software engineer.",
            is_profile_completed=True,
            profile_status="VERIFIED",
            is_photo_visible=True,
            is_verified=True,
            is_active=True,
        )

        self.url = reverse("search_profiles")

    # --------------------------------------------------
    # TEST 1: Get all active and verified profiles
    # --------------------------------------------------

    def test_get_all_profiles(self):

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data["data"]),
            3,
        )

    # --------------------------------------------------
    # TEST 2: Filter by gender
    # --------------------------------------------------

    def test_filter_by_gender(self):

        response = self.client.get(self.url, {"gender": "FEMALE"})

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data["data"]),
            2,
        )

        for profile in response.data["data"]:
            self.assertEqual(
                profile["gender"],
                "FEMALE",
            )

    # --------------------------------------------------
    # TEST 3: Filter by occupation
    # --------------------------------------------------

    def test_filter_by_occupation(self):

        response = self.client.get(self.url, {"occupation": "Engineer"})

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data["data"]),
            2,
        )

        for profile in response.data["data"]:
            self.assertIn(
                "Engineer",
                profile["occupation"],
            )

    # --------------------------------------------------
    # TEST 4: Filter by education
    # --------------------------------------------------

    def test_filter_by_education(self):

        response = self.client.get(self.url, {"education": "B.Tech"})

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data["data"]),
            2,
        )

    # --------------------------------------------------
    # TEST 5: Filter by height
    # --------------------------------------------------

    def test_filter_by_height_range(self):

        response = self.client.get(
            self.url,
            {
                "min_height": "5.7",
                "max_height": "6.0",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data["data"]),
            2,
        )

    # --------------------------------------------------
    # TEST 6: Filter by income
    # --------------------------------------------------

    def test_filter_by_income_range(self):

        response = self.client.get(
            self.url,
            {
                "min_income": "600000",
                "max_income": "1000000",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data["data"]),
            2,
        )

    # --------------------------------------------------
    # TEST 7: Filter by marital status
    # --------------------------------------------------

    def test_filter_by_marital_status(self):

        response = self.client.get(self.url, {"marital_status": "NEVER_MARRIED"})

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data["data"]),
            3,
        )

    # --------------------------------------------------
    # TEST 8: Filter by denomination
    # --------------------------------------------------

    def test_filter_by_denomination(self):

        response = self.client.get(self.url, {"denomination": self.denomination.id})

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data["data"]),
            3,
        )

    # --------------------------------------------------
    # TEST 9: Multiple filters
    # --------------------------------------------------

    def test_multiple_filters(self):

        response = self.client.get(
            self.url,
            {
                "gender": "FEMALE",
                "occupation": "Engineer",
                "min_height": "5.5",
                "max_height": "6.0",
            },
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            len(response.data["data"]),
            1,
        )

        self.assertEqual(
            response.data["data"][0]["profile_id"],
            "MAT000001",
        )

    # --------------------------------------------------
    # TEST 10: No matching profile
    # --------------------------------------------------

    def test_no_matching_profile(self):

        response = self.client.get(self.url, {"occupation": "Pilot"})

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        self.assertEqual(
            response.data["data"],
            [],
        )

    # --------------------------------------------------
    # TEST 11: Inactive profile should not appear
    # --------------------------------------------------

    def test_inactive_profile_not_returned(self):

        self.profile1.is_active = False
        self.profile1.save()

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        profile_ids = [profile["profile_id"] for profile in response.data["data"]]

        self.assertNotIn(
            "MAT000001",
            profile_ids,
        )

    # --------------------------------------------------
    # TEST 12: Unverified profile should not appear
    # --------------------------------------------------

    def test_unverified_profile_not_returned(self):

        self.profile1.is_verified = False
        self.profile1.save()

        response = self.client.get(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        profile_ids = [profile["profile_id"] for profile in response.data["data"]]

        self.assertNotIn(
            "MAT000001",
            profile_ids,
        )
