from .models import Church
from django.shortcuts import get_object_or_404


class ChurchService:

    @staticmethod
    def create_church(validated_data):
        """
        Create a new church.
        """

        church = Church.objects.create(**validated_data)

        return church

    def update_church(church_id, validated_data):
        church = get_object_or_404(Church, id=church_id)

        for key, value in validated_data.items():
            setattr(church, key, value)

        church.save()

        return church

    @staticmethod
    def get_all_churches():
        """
        Retrieve all churches.
        """
        return Church.objects.all()

    @staticmethod
    def get_church_by_id(church_id):
        """
        Retrieve a church by its ID.
        """
        return get_object_or_404(Church, id=church_id)

    @staticmethod
    def delete_church(church_id):
        """
        Delete a church by its ID.
        """
        church = get_object_or_404(Church, id=church_id)
        church.delete()

        return True

    @staticmethod
    def approve_church(church_id):
        """
        Approve a church by its ID.
        """
        church = get_object_or_404(Church, id=church_id)
        church.verification_status = Church.VerificationStatus.APPROVED
        church.save()

        return church

    @staticmethod
    def reject_church(church_id):
        """
        Reject a church by its ID.
        """
        church = get_object_or_404(Church, id=church_id)
        church.verification_status = Church.VerificationStatus.REJECTED
        church.save()

        return church

    @staticmethod
    def get_approved_churches():
        """
        Retrieve all approved churches.
        """
        return Church.objects.filter(
            verification_status=Church.VerificationStatus.APPROVED
        )

    @staticmethod
    def get_all_rejected_churches():
        """
        Retrieve all rejected churches.
        """
        return Church.objects.filter(
            verification_status=Church.VerificationStatus.REJECTED
        )

    @staticmethod
    def get_all_pending_churches():
        """
        Retrieve all pending churches.
        """
        return Church.objects.filter(
            verification_status=Church.VerificationStatus.PENDING
        )

    @staticmethod
    def activate_church(church_id):
        """
        Activate a church by its ID.
        """
        church = get_object_or_404(Church, id=church_id)
        church.is_active = True
        church.save()

        return church

    @staticmethod
    def deactivate_church(church_id):
        """
        Deactivate a church by its ID.
        """
        church = get_object_or_404(Church, id=church_id)
        church.is_active = False
        church.save()

        return church

    @staticmethod
    def get_total_churches():
        """
        Get the total number of churches.
        """
        return Church.objects.count()

    @staticmethod
    def get_list_of_active_churches():
        """
        Retrieve a list of all active churches.
        """
        return Church.objects.filter(is_active=True)

    @staticmethod
    def get_list_of_inactive_churches():
        """
        Retrieve a list of all inactive churches.
        """
        return Church.objects.filter(is_active=False)

    @staticmethod
    def get_church_by_branch_id(branch_id):
        """
        Retrieve churches by branch ID.
        """
        return Church.objects.filter(branch_id=branch_id)

    @staticmethod
    def get_church_by_city(city):
        """
        Retrieve churches by city.
        """
        return Church.objects.filter(city__iexact=city)

    @staticmethod
    def get_churches_names_by_city(city):
        """
        Retrieve names of churches by city.
        """
        churches_names = Church.objects.filter(city__iexact=city).values_list(
            "name", flat=True
        )
        return churches_names.name
