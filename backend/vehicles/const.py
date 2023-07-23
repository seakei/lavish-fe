from django.utils.translation import gettext_lazy as _

# Booking Type
APPOINTMMENT = 1
CLAIM_APPOINTMENT = 2
SURVEY_APPOINTMENT = 3
BALANCE_APPOINTMENT = 4
COATING_MAINTENANCE_APPOINTMENT = 5
BOOKING_TYPE = (
    (APPOINTMMENT, _("Appointment")),
    (CLAIM_APPOINTMENT, _("Claim Appointment")),
    (SURVEY_APPOINTMENT, _("Survey Appointment")),
    (BALANCE_APPOINTMENT, _("Balance Appointment")),
    (COATING_MAINTENANCE_APPOINTMENT, _("Coating Maintenance Appointment")),
)