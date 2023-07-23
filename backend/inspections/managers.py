from django.db import models
from django.db.models.query import QuerySet

class InspectionCustomManager(models.Manager):
    pass
    
class InspectionQuerySet(models.QuerySet):
    def inspection_queryset_method(self):
        return self.get()
    
    def get_inspections_active_only(self):
        return self.filter(is_active=True,)
    
class SignatureCustomManager(models.Manager):
    pass

class SignatureQuerySet(models.QuerySet):
    def signature_queryset_method(self):
        return self.get()

    def inspection_siggys_active_only(self):
        return self.filter(is_active=True,)
    
class InspectionPictureCustomManager(models.Manager):
    pass

class InspectionPictureQuerySet(models.QuerySet):
    def inspection_queryset_method(self):
        return self.get()
    
    def inspection_pics_active_only(self):
        return self.filter(is_active=True,)
    

InspectionManager = InspectionCustomManager.from_queryset(InspectionQuerySet)
SignatureManager = SignatureCustomManager.from_queryset(SignatureQuerySet)
InspectionUploadManager = InspectionPictureCustomManager.from_queryset(InspectionPictureQuerySet)