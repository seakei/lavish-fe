import base64
from django.contrib.auth import get_user_model
from salesorders.models import SalesOrder, Order, OrderItem, Signature
from inspections.models  import Inspection
# from salesorders.const import (
#     ORDER_TYPE, ORDER_MODE, PRODUCT_PACKAGE,
#     VEHICLE_PART, JOB_TYPE, ITEM_NAME,
#     PART_STATUS, ACCESSORIES, ITEM_NAME
# )
from vehicles.models import Booking

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
def create_inspection(order_item):
    order_item.refresh_from_db()
    inspection_obj = Inspection.objects.create(order_item = order_item)

def update_inspection(order_item, **kwargs):
    order_item_uuid = order_item.get('uuid')
    inspection_obj = Inspection.objects.get(pk=order_item_uuid)
    inspection_attrs = kwargs.get('inspection', {})
    for k, v in inspection_attrs.items():
                setattr(inspection_obj, k, v)
                inspection_obj.save() 

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

