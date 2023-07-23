import base64
import binascii
from rest_framework import serializers
from vehicles.models import Booking
from salesorders.models import (
    SalesOrder,
    Order,
    OrderItem,
    Signature
)
from salesorders.const import (
    CUST_REQUIREMENT,
    JOB_TYPE,
    PRODUCT_PACKAGE,
    ORDER_MODE,
    ITEM_NAME,
    PART_STATUS,
    # ACCESSORIES,
    SURCHARGE_VEHICLE_TYPE,
    TEAM_TYPE,
    VEHICLE_PART,
    DISCOUNT_TYPE,
    ORDER_TYPE,
)

from ..fields import ChoiceField

class BinarySerializerField(serializers.Field):
    def to_representation(self, value):
        if value is not None:
            base64_data = base64.b64encode(value).decode()
            return base64_data
        return None
        pass

    def to_internal_value(self, data):
        try:
            if data:
                return base64.b64decode(data)
            else:
                return None         
        except (TypeError, binascii.Error):
            raise serializers.ValidationError('Invalid base64 string')
        
    #OPT : do another for taking in byte

class OrderItemSerializer(serializers.ModelSerializer):

    # vehicle_part = ChoiceField(choices = VEHICLE_PART, required = False)
    job_type = ChoiceField(choices = JOB_TYPE, required = False)
    # item_name = ChoiceField(choices = ITEM_NAME, required = False)
    status = ChoiceField(choices = PART_STATUS, required = False)
    # to_accessories = ChoiceField(choices = ACCESSORIES, required = False)
    # addon = ChoiceField(choices = ITEM_NAME, required = False)

    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    orderitems = serializers.SerializerMethodField()

    order_type = ChoiceField(choices = ORDER_TYPE, required = False)
    order_mode = ChoiceField(choices = ORDER_MODE, required = False)
    product_package = ChoiceField(choices = PRODUCT_PACKAGE, required = False)

    def get_orderitems(self, order):
        orders = order.order.all()
        orderitem_serializer = OrderItemSerializer(orders, many=True)
        return orderitem_serializer.data
    
    class Meta:
        model = Order
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class SignatureSerializer(serializers.ModelSerializer):
    signature_data = BinarySerializerField()

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'signature_data' in validated_data:
            instance.signature_data = validated_data['signature_data']
            instance.save()
        return instance
    
    class Meta:
        model = Signature
        fields = ('signature_data',)

class SalesOrderSerializer(serializers.ModelSerializer):
    booking = BookingSerializer()
    orders = serializers.SerializerMethodField()
    
    cust_requirement = ChoiceField(choices = CUST_REQUIREMENT, required = True)
    assigned_team = ChoiceField(choices = TEAM_TYPE, required = True)
    surcharge_type = ChoiceField(choices = SURCHARGE_VEHICLE_TYPE, required = False)
    discount_type = ChoiceField(choices = DISCOUNT_TYPE, required = False)

    class Meta:
        model = SalesOrder
        # fields = (
        #     'uuid', 
        #     'installment_plan', 
        #     'cust_requirement', 'duration', 
        #     'assigned_team', 'tint_price', 
        #     'surcharge_type', 'surcharge_price', 
        #     'upgrade_or_alacarte', 'remove_charge', 
        #     'sun_visor_charge', 'discount_bool', 
        #     'discount_type','discount_amount',
        #     'cust_reference_bool', 'reference_fee', 
        #     'total_amount', 'balance_amount', 'number', 
        #     'signature_id','booking', 'orders',
        #     'is_active','created_by', 'updated_by'
        # )

        fields = '__all__'

    def get_orders(self, sales_order):
        salesorder = sales_order.salesorder.all()
        order_serializer = OrderSerializer(salesorder, many=True)
        return order_serializer.data
    
    def create(self, validated_data):
        booking = validated_data.pop('booking', None)
        order_serializer = OrderSerializer(validated_data, many=True)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data.pop('booking', None)
        order_serializer = OrderSerializer(validated_data, many=True)
        return super().update(instance, validated_data)
