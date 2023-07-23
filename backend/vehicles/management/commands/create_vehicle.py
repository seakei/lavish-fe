import logging
from datetime import datetime

from faker import Faker

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils.translation import gettext_lazy as _

from vehicles.models import Booking, Vehicle, BusinessPartner


logger = logging.getLogger(__name__)


CAR_BRANDS = (
    "Toyota Camry",
    "Toyota Vios",
    "Honda BRV",
    "Honda City",
    "Mercedes Benz CLA",
    "Porsche Macan",
    "Proton X50",
    "BMW 320i",
)
PACKAGES = (
    "Tint package",
    "Coating package",
    "PPF ala-carte",
    "Tint + coating package",
    "Coating ala-carte",
)
LANGUAGES = ('EN', 'CN', 'MS')
ORIGIN = (
    'Existing Customer - Voucher',
    'Facebook - FB-TINT',
    'Google - GC-COAT',
    'Walk In - Organic',
    'Referral - No Voucher',
    'YouTube',
)
BOOKING_TYPE = (1, 2, 3, 4, 5)
REMARKS = ("Tint Survey", "Install Tint", "Coating")

fake = Faker()

UserModel = get_user_model()

user = UserModel.objects.get(email="superoot@lavishfilm.com")


class Command(BaseCommand):
    """
    Setup vehicle
    """

    help = "Create sample vehicles"

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=int, default=1)

        parser.add_argument(
            '-c',
            '--commit',
            action='store_true',
            dest='commit',
            default=False,
            help="Confirmation",
        )

    def random_date(self) -> datetime:
        today = datetime.now().strftime("%Y-%m-%d")

        random_hour = fake.random_int(min=10, max=18)
        random_minute = fake.random_int(min=0, max=30, step=30)
        random_datetime = f"{today} {random_hour}:{random_minute}:00"

        random_timeslot = datetime.strptime(random_datetime, '%Y-%m-%d %H:%M:%S')

        print(random_timeslot)

        return random_timeslot

    def setup_vehicle(self):
        vehicleKwargs = {}

        vehicleKwargs['created_by'] = user
        vehicleKwargs['car_plate'] = fake.bothify(
            text="???####", letters="ABCDEFGHJKLMNPQRTUVWXY"
        )
        vehicleKwargs['car_brand'] = fake.random_element(elements=CAR_BRANDS)
        vehicleKwargs['branch'] = fake.random_int(min=1, max=5)
        vehicleKwargs['package'] = fake.random_element(elements=PACKAGES)
        vehicleKwargs['partner_id'] = self.setup_partner()

        vehicle = Vehicle.objects.create(**vehicleKwargs)

        booking = self.setup_booking(vehicle.uuid)

        return vehicle

    def setup_partner(self):
        partnerKwargs = {}

        partnerKwargs['created_by'] = user
        partnerKwargs['phone_number'] = fake.msisdn()
        partnerKwargs['name'] = fake.name()
        partnerKwargs['email'] = fake.email()
        partnerKwargs['language'] = fake.random_element(elements=LANGUAGES)
        partnerKwargs['customer_from'] = fake.random_element(elements=ORIGIN)

        partner = BusinessPartner.objects.create(**partnerKwargs)

        return partner.uuid

    def setup_booking(self, vehicle_uuid):
        bookingKwargs = {}

        bookingKwargs['created_by'] = user
        bookingKwargs['booking_date'] = self.random_date()
        bookingKwargs['booking_duration'] = fake.random_int(min=1, max=4)
        bookingKwargs['booking_type'] = fake.random_element(elements=BOOKING_TYPE)
        bookingKwargs['remark'] = fake.random_element(elements=REMARKS)
        bookingKwargs['vehicle_id'] = vehicle_uuid

        booking = Booking.objects.create(**bookingKwargs)

        return booking.uuid

    @transaction.atomic
    def handle(self, *args, **options):
        sid = transaction.savepoint()

        count = options.get('number', 1)
        commit = options.get('commit', False)

        for _ in range(count):
            vehicle = self.setup_vehicle()

            print(f"Created vehicle: {vehicle.uuid} - Car plate {vehicle.car_plate}")

        if commit:
            transaction.savepoint_commit(sid)
            logger.info(self.style.SUCCESS("Successful commit"))
            print("Commit completed. Changes were made.")
        else:
            transaction.savepoint_rollback(sid)
            logger.info(self.style.WARNING("Successful dry-run"))
            print("Dry-run completed. No changes were made.")
