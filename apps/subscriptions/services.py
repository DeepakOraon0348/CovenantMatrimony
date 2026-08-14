
from .models import SubscriptionPlan


class SubscriptionPlanService:

    @staticmethod
    def create_subscription_plan(validated_data):
        return SubscriptionPlan.objects.create(
            **validated_data
        )

    @staticmethod
    def get_subscription_plan(plane_id):
        return SubscriptionPlan.objects.get(
            id=plane_id
        )

    @staticmethod
    def get_all_subscription_plans():
        return SubscriptionPlan.objects.all().order_by(
            "price"
        )

    @staticmethod
    def update_subscription_plan(
        plan_id,
        validated_data
    ):
        plan = SubscriptionPlan.objects.get(
            id=plan_id
        )

        for field, value in validated_data.items():
            setattr(plan, field, value)

        plan.save()

        return plan

    @staticmethod
    def delete_subscription_plan(plane_id):
        plan = SubscriptionPlan.objects.get(
            id=plane_id
        )

        plan.delete()

        return True

