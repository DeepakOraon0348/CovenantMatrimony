import code
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from apps.documents.serializers import DocumentSerializer
from apps.family.serializers import FamilySerializer
from apps.marriages.serializers import MarriageSerializer
from apps.matchmaking.models import InterestRequest, Match
from apps.matchmaking.serializers import InterestRequestSerializer, MatchSerializer
from apps.meetings.models import Meeting
from apps.meetings.serializers import MeetingSerializer
from apps.prayers.models import Prayer
from apps.prayers.serializers import PrayerSerializer
from apps.profiles.serializers import ProfileSerializers
from apps.subscriptions.models import *
from apps.branches.models import *
from apps.churches.models import *
from apps.documents.models import *
from apps.family.models import *
from apps.marriages.models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from apps.user_subscriptions.models import UserSubscription
from apps.user_subscriptions.serializers import UserSubscriptionSerializer

from .serializers import *
from .services import *


# Create your views here.
class CreateAccountAPI(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User_registration = RegisterUserService.user_registration(
            serializer.validated_data
        )

        return Response(
            {
                "message": "User Register Sucessful.",
                "data": RegisterUserSerializer(User_registration).data,
            },
            status=status.HTTP_201_CREATED,
        )


class UserLoginAPI(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        login_response = RegisterUserService.user_login(serializer.validated_data)

        return Response(
            {
                "message": "Login Successful.",
                "data": login_response,
            },
            status=status.HTTP_200_OK,
        )


class GetAllRegisterUser(APIView):
    def get(self, request):
        user = RegisterUserService.get_all_register_user()
        serializer = RegisterUserSerializer(user, many=True)
        return Response(
            {"message": "Get All Register User.", "data": serializer.data},
            status=status.HTTP_200_OK,
        )


class NumbersOfRegisterUserAPI(APIView):
    def get(self, request):
        numbersOfuser = RegisterUserService.numbers_of_users()
        serializer = RegisterUserSerializer(numbersOfuser, many=True)
        return Response(
            {
                "message": "Total Numbers of Register Users.",
                "total": len(serializer.data),
            },
            status=status.HTTP_200_OK,
        )

class MyDashboardAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        profile = Profile.objects.filter(
            user=user
        ).first()

        subscription = (
            UserSubscription.objects
            .filter(
                user=user,
                is_active=True,
            )
            .order_by("-created_at")
            .first()
        )
        document= Document.objects.filter(profile=profile.id)
        family= Family.objects.filter(profile=profile.id)

        sent_interests = InterestRequest.objects.filter(
            sender_profile__user=user
        )

        received_interests = InterestRequest.objects.filter(
            receiver_profile__user=user
        )

        matches = Match.objects.filter(
            interest_request__sender_profile__user=user
        ) | Match.objects.filter(
            interest_request__receiver_profile__user=user
        )

        meetings = Meeting.objects.filter(
            match__in=matches
        )

        marriages = Marriage.objects.filter(
            meeting__in=meetings
        )
        print("Church:", user.church)
        print("Church ID:", user.church.id)
        prayers = Prayer.objects.filter(church=user.church.id)
        print("Prayer count:", prayers.count())
        print("Prayers:", list(prayers))
    

        return Response(
            {
                "message": "Dashboard data fetched successfully.",
                "data": {
                    "profile": (
                        ProfileSerializers(profile).data
                        if profile else None
                    ),

                    "subscription": (
                        UserSubscriptionSerializer(
                            subscription
                        ).data
                        if subscription else None
                    ),

                    "interests": {
                        "sent": InterestRequestSerializer(
                            sent_interests,
                            many=True
                        ).data,

                        "received": InterestRequestSerializer(
                            received_interests,
                            many=True
                        ).data,
                    },

                    "matches": MatchSerializer(
                        matches.distinct(),
                        many=True
                    ).data,

                    "meetings": MeetingSerializer(
                        meetings,
                        many=True
                    ).data,

                    "marriages": MarriageSerializer(
                        marriages,
                        many=True
                    ).data,

                    "prayers": PrayerSerializer(
                        prayers,
                        many=True
                    ).data,
                    
                    "document":DocumentSerializer(
                        document,
                        many=True
                    ).data,
                    
                    "family":FamilySerializer(family, many=True).data,
                }
            },
            status=status.HTTP_200_OK
        )
