import base64
from django.contrib.auth import get_user_model
from salesorders.models import SalesOrder, Order, OrderItem, Signature
from salesorders.const import (
    ORDER_TYPE, ORDER_MODE, PRODUCT_PACKAGE,
    VEHICLE_PART, JOB_TYPE, ITEM_NAME,
    PART_STATUS, ACCESSORIES, ITEM_NAME
)
from vehicles.models import Booking
from inspections.services import create_inspection, update_inspection

UserModel = get_user_model()

def ConvertStringToEnumVal(choices, data):
    result = None              

    if type(data) == list:
         result = []
         for item in data:
              for key, label in choices:
                if str(item) == label:
                    result.append(key)
                    break
    else:          
        for key, label in choices:
            if str(data) == label:
                result = key
                break

    if result is None:
            return None

    return result

def handle_salesorder_order_orderitems(salesorder, **kwargs):
    # handle multiple orders + orderitems branching down
    salesorder.refresh_from_db()
    orders = kwargs.get('orders', {})

    booking = kwargs.get('booking', {})
    if orders:
        for order_attrs in orders:
            order_uuid = order_attrs.pop('uuid', None)
            order_items = order_attrs.pop('orderitems', None)

            order_types = order_attrs.get('order_type', None)
            order_mode = order_attrs.get('order_mode', None)
            product_package = order_attrs.get('product_package', None)

            if order_types:
                order_attrs['order_type'] = ConvertStringToEnumVal(ORDER_TYPE, order_types)
            if order_mode:
                order_attrs['order_mode'] = ConvertStringToEnumVal(ORDER_MODE, order_mode)
            if product_package:
                order_attrs['product_package'] = ConvertStringToEnumVal(PRODUCT_PACKAGE, product_package)

            order = Order.objects.get(pk=order_uuid) if order_uuid else None
            if order:
                order_attrs.pop('salesorder', None)
                for k, v in order_attrs.items():
                            setattr(order, k, v)
                            order.save()
                if order_items:
                    save_order_items(order, order_items)
            else:
                order = Order.objects.create(salesorder = salesorder, **order_attrs)
                save_order_items(order, order_items)
    
    if booking:
        booking_uuid = booking.get('uuid')
        booking_obj = Booking.objects.get(pk=booking_uuid)
        if booking_obj:
            salesorder.booking = booking_obj
            salesorder.save()

def save_order_items(order, order_items):
     for order_item_attrs in order_items:
        order_item_attrs.pop('order', None)
        order_item_uuid = order_item_attrs.pop('uuid', None)

        vehicle_part = order_item_attrs.get('vehicle_part', None)
        job_type = order_item_attrs.get('job_type', None)
        item_name = order_item_attrs.get('item_name', None)
        status = order_item_attrs.get('status', None)
        to_accessories = order_item_attrs.get('to_accessories', None)
        addon = order_item_attrs.get('addon', None)

        # if vehicle_part:
        #     order_item_attrs['vehicle_part'] = ConvertStringToEnumVal(VEHICLE_PART, order_item_attrs['vehicle_part'])
        if job_type:
            order_item_attrs['job_type'] = ConvertStringToEnumVal(JOB_TYPE, order_item_attrs['job_type'])
        # if item_name:
        #     order_item_attrs['item_name'] = ConvertStringToEnumVal(ITEM_NAME, order_item_attrs['item_name'])
        if status:
            order_item_attrs['status'] = ConvertStringToEnumVal(PART_STATUS, order_item_attrs['status'])
        # if to_accessories:
        #     order_item_attrs['to_accessories'] = ConvertStringToEnumVal(ACCESSORIES, order_item_attrs['to_accessories'])
        # if addon:
        #     order_item_attrs['addon'] = ConvertStringToEnumVal(ITEM_NAME, order_item_attrs['addon'])

        

        order_item = OrderItem.objects.get(pk=order_item_uuid) if order_item_uuid else None
        if order_item:
            for k, v in order_item_attrs.items():
                setattr(order_item, k, v)
                order_item.save()
        else:
            created_order_item = OrderItem.objects.create(order = order, **order_item_attrs) 
            create_inspection(created_order_item)  

def create_signature_entry(salesorder, **kwargs):
     signature = kwargs.get('signature', {})
     data = signature.get('signature_data', None)
     if data:
        signature['signature_data'] = base64.b64decode(data)
     siggy = Signature.objects.create(salesorder = salesorder, **signature) 
     setattr(salesorder, 'signature_id', siggy.uuid)
     salesorder.save()

def update_signature_entry(**kwargs):
     signature_attrs = kwargs.get('signature', {})
     uuid = signature_attrs.pop('uuid', None)
     signature_obj = Signature.objects.get(pk=uuid) if uuid else None
     if signature_obj:
            for k, v in signature_attrs.items():
                setattr(signature_obj, k, v)
                signature_obj.save()

