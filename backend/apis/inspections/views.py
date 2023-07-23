# # -*- coding: utf-8 -*-
import os
from django.core.files.storage import default_storage
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from apis.inspections.serializers import InspectionSerializer,InspectionSignatureSerializer, InspectionUploadSerializer
from inspections.models import Inspection, InspectionUpload, InspectionSignature

UserModel = get_user_model()


class InspectionViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionSerializer
    queryset = Inspection.objects.get_inspections_active_only()

class InspectionSignatureViewSet(viewsets.ModelViewSet):
    serializer_class = InspectionSignatureSerializer
    queryset = InspectionSignature.objects.inspection_siggys_active_only()

class InspectionUploadViewset(viewsets.ModelViewSet):
    serializer_class = InspectionUploadSerializer
    parser_classes = (MultiPartParser, FormParser)
    queryset = InspectionUpload.objects.inspection_pics_active_only()
    # queryset = InspectionUpload.objects.all()

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def perform_destroy(self, instance):
        if instance.upload_file:
            file_path = os.path.join(instance.inspection.number, instance.upload_file.path)
            default_storage.delete(file_path)
        return super().perform_destroy(instance)
    

    