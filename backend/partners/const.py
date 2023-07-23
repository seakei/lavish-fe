from django.utils.translation import gettext_lazy as _

PERSON = 1
GROUP = 2
COMPANY = 3
CATEGORY_CHOICES = (
    (PERSON, _("Person")),
    (GROUP, _("Group")),
    (COMPANY, _("Company"))
)


NEW = 1
APPOINTMENT = 2
VERIFIED = 3
BANNED = 4
BLACKLISTED = 5

PROFILE_STATUS_CHOICES = (
    (NEW, _("New")),
    (APPOINTMENT, _("Appointment")),
    (VERIFIED, _("Verified")),
    (BANNED, _("Banned")),
    (BLACKLISTED, _("Blacklisted")),
)


ADMINISTRATOR = 1
CUSTOMER = 2
TELEMARKETER_LEAD = 3
TELEMARKETER = 4
INDOOR_SALES_LEAD = 5
INDOOR_SALES = 6
TECHNICIAN_LEAD = 7
TECHNICIAN = 8

ROLE_CHOICES = (
    (ADMINISTRATOR, _("Administrator")),
    (TELEMARKETER_LEAD, _("Telemarketer Lead")),
    (TELEMARKETER, _("Telemarketer")),
    (INDOOR_SALES_LEAD, _("Indoor Sales Lead")),
    (INDOOR_SALES, _("Indoor Sales")),
    (TECHNICIAN_LEAD, _("Technician Lead")),
    (TECHNICIAN, _("Technician")),
    (CUSTOMER, _("Customer")),
)


PUCHONG = 1
KOTA_DAMANSARA = 2
SHAMELIN = 3
KAJANG = 4
BALAKONG = 5

BRANCH_CHOICES = (
    (PUCHONG, _("Bandar Puteri, Puchong (HQ)")),
    (KOTA_DAMANSARA, _("Kota Damansara Branch")),
    (SHAMELIN, _("Shamelin, KL Branch")),
    (KAJANG, _("Kajang Branch")),
    (BALAKONG, _("Balakong Branch")),
)
