import logging

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

from vehicles.models import (
    Booking, Vehicle, BusinessPartner
)
from salesorders.models import(
    SalesOrder, Order, OrderItem, Signature
)

from salesorders.const import *

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    """
    Setup vehicle + booking + sales order + order + orderitem
    """
    help = "Create Sales order data"

    def add_arguments(self, parser):
        parser.add_argument(
            '--commit',
            '-c',
            action='store_true',
            dest='commit',
            default=False,
            help="Confirmation"
        )

    def setup_vehicle_and_booking(self):
        partnerKwargs = {
            "phone_number": "0129999219",
            "name": "ddly",
            "email": "ddly@mailinator.com",
            "language": "English",
            "address": "Kaptong",
            "customer_from": "Hell"
        }
        partner = BusinessPartner.objects.create(**partnerKwargs)

        kwargs = {
        "car_plate": "KEN99999",
        "car_brand": "Toyota",
        "branch": "Kajang Branch",
        "package": "PPF ala-carte",
        "remarks": "Just a field to write anything regarding this car",
        "partner_id": partner.uuid,
        }    
        vehicle = Vehicle.objects.create(**kwargs)

        bookingKwargs = {
                "booking_date": "2023-06-06T21:00",
                "follow_up_date": None,
                "vehicle_id": vehicle.uuid
            }
        booking = Booking.objects.create(**bookingKwargs)
        return booking

    def setup_salesorder(self, bookingId):
        kwargs = {
            # "orders": [],
            # "orderitems": [],
            "is_active": True,
            "installment_plan": False,
            "cust_requirement": EASY,
            "duration": 1,
            "assigned_team": TEAM_B,
            "surcharge_type": NIL,
            "surcharge_price": None,
            "upgrade_or_alacarte": False,
            "remove_charge": 300,
            "sun_visor_charge": 0,
            "discount": True,
            "discount_type": FIVEPC,
            "discount_amount": 50, # todo should auto count
            "cust_reference": False,
            "reference_fee": 500,
            "total_amount": 2000,
            "balance_amount": 100,
            "sales_person_in_charge": None,
            "booking_id": bookingId
        }
        salesorder = SalesOrder.objects.create(**kwargs)

        orderInfo = {
            "item_price": 1000,
            "is_active": True,
            "order_type": TINT,
            "order_mode": PACKAGE,
            "product_package": SILVER,
            "salesorder_id": salesorder.uuid
        }
        order = Order.objects.create(**orderInfo)

        order_items = [
            {
                "order_id": order.uuid,
                "is_active": True,
                "vehicle_part": FRONTWINDSCREEN,
                "claim_insurance": True,
                "job_type": [REMOVE_OLD, INSTALL],
                "item_name": JASPER_2MIL,
                "remarks": None,
                "status": None,
                "to_accessories": None,
                "addon": CARBONFILM_BK70_2MIL,
            },
            {
                "order_id": order.uuid,
                "is_active": True,
                "vehicle_part": REARWINDSCREEN,
                "claim_insurance": None,
                "job_type": [REMOVE_OLD, INSTALL],
                "item_name": JASPER_2MIL,
                "remarks": None,
                "status": None,
                "to_accessories": None,
                "addon": CARBONFILM_BK90_2MIL,
            },
            {
                "order_id": order.uuid,
                "is_active": True,
                "vehicle_part": SIDEWINDOWLEFTONE,
                "remarks": "Gentle pls",
            },
            {
                "order_id": order.uuid,
                "is_active": True,
                "vehicle_part": FREEGIFT,
                "job_type": [DO_NOW],
                "status": REMAIN,
                "to_accessories": None,
            },
            {
                "order_id": order.uuid,
                "is_active": True,
                "vehicle_part": FREEGIFT,
                "job_type": [PENDING],
                "status": CHANGEFOC,
                "to_accessories": None,
            }
        ]

        for item in order_items:
            OrderItem.objects.create(**item)

        siggyInfo = {
            "is_active": True,
            "salesorder_id": salesorder.uuid
        }
        siggy = Signature.objects.create(**siggyInfo)

        salesorder.signature_id = siggy.uuid
        salesorder.save()
    
    @transaction.atomic
    def handle(self, **options):
        sid = transaction.savepoint()

        booking = self.setup_vehicle_and_booking()
        salesorder = self.setup_salesorder(booking.uuid)
        # order = self.setup_order(salesorder.uuid)

        if options['commit']:
            logger.info(self.style.SUCCESS("Successful commit"))
            transaction.savepoint_commit(sid)
        else:
            logger.info(self.style.WARNING("Successful dry-run"))
            transaction.savepoint_rollback(sid)
