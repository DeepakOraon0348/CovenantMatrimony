from .models import Branch
from django.shortcuts import get_object_or_404


class BranchService:

    @staticmethod
    def create_branch(validated_data):
        """
        Create a new branch.
        """

        branch = Branch.objects.create(**validated_data)

        return branch

    @staticmethod
    def update_branch(branch_id, validated_data):

        branch = get_object_or_404(Branch, id=branch_id)

        for key, value in validated_data.items():
            setattr(branch, key, value)

        branch.save()

        return branch

    @staticmethod
    def get_all_branches():

        return Branch.objects.all()

    @staticmethod
    def Delete_branch(branch_id):
        print(branch_id)
        branch = get_object_or_404(Branch, id=branch_id)
        print(branch)
        branch.delete()

        return True

    @staticmethod
    def Approve_Branch(branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        branch.verification_status = Branch.VerificationStatus.APPROVED

        branch.save()
        return branch

    @staticmethod
    def get_city_branch(city):
        branches = get_object_or_404(Branch, city=city)
        return branches

    @staticmethod
    def Reject_Branch(branch_id):
        branch = get_object_or_404(Branch, id=branch_id)

        branch.verification_status = Branch.VerificationStatus.REJECTED
        branch.save()

        return branch

    @staticmethod
    def Activate_Branch(branch_id):
        branch = get_object_or_404(Branch, id=branch_id)

        branch.is_active = True
        branch.save()

        return branch

    @staticmethod
    def Deactivate_Branch(branch_id):
        branch = get_object_or_404(Branch, id=branch_id)
        branch.is_active = False
        branch.save()

        return branch

    @staticmethod
    def Count_Branch():
        branches = Branch.objects.all()
        count = branches.count()

        return count

    @staticmethod
    def Approved_Branch():
        branches = Branch.objects.filter(verification_status="APPROVED").count()

        return branches

    @staticmethod
    def Approved_Branches():
        branches = Branch.objects.filter(
            verification_status=Branch.VerificationStatus.APPROVED
        )

        return branches

    @staticmethod
    def Pending_Branches():
        branches = Branch.objects.filter(
            verification_status=Branch.VerificationStatus.PENDING
        )

        return branches.count()

    @staticmethod
    def List_Of_Pendign_branch():
        branches = Branch.objects.filter(
            verification_status=Branch.VerificationStatus.PENDING
        )
        return branches
