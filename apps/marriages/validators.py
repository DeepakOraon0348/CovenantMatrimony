from django.core.exceptions import ValidationError


def validate_marriage_date(
    marriage_date,
    meeting,
):

    if marriage_date < meeting.meeting_date:

        raise ValidationError(
            "Marriage date cannot be before the meeting date."
        )