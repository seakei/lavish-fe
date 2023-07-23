import base64
import binascii
import os
from django.core.files.storage import default_storage
from rest_framework import serializers
from inspections.models import (
    Inspection,
    InspectionSignature,
    InspectionUpload,
)
from apis.salesorders.serializers import OrderItemSerializer

#from ..fields import ChoiceField

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
        

class InspectionSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer()
    class Meta:
        model = Inspection
        fields = '__all__'

    def get_inspection(self, inspection):
        inspection.inspection.all()
        return 

    def update(self, instance, validated_data):
        validated_data.pop('orderitem', None)
        return super().update(instance, validated_data)
    
#might wanna change siggy to normal file
class InspectionSignatureSerializer(serializers.ModelSerializer):
    signature_data = BinarySerializerField()

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'signature_data' in validated_data:
            instance.signature_data = validated_data['signature_data']
            instance.save()
        return instance
    
    class Meta:
        model = InspectionSignature
        fields = ('signature_data',)

class InspectionUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionUpload
        fields = '__all__'
        extra_kwargs = {
            'upload_file': {'use_url': True}
        }

    def create(self, validated_data):
        upload_file = serializers.FileField()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        upload_file = serializers.FileField()

        if instance.upload_file:
            file_path = os.path.join(instance.inspection.number, instance.upload_file.path)
            default_storage.delete(file_path)

        if 'upload_file' in validated_data:
            instance.upload_file = validated_data['upload_file']
            instance.save()
        return instance
