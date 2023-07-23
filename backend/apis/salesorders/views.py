# # -*- coding: utf-8 -*-
# from rest_framework import permissions
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, JSONParser
from .serializers import SalesOrderSerializer, OrderItemSerializer, OrderSerializer, SignatureSerializer
from salesorders.models import SalesOrder, Order, OrderItem, Signature
from salesorders.services import handle_salesorder_order_orderitems, create_signature_entry, update_signature_entry

UserModel = get_user_model()

class SalesOrderViewSet(viewsets.ModelViewSet):
    serializer_class = SalesOrderSerializer
    queryset = SalesOrder.objects.all()
    # parser_classes = (MultiPartParser, FormParser, JSONParser, FileUploadParser)

    def test_method(request):
        return HttpResponse("derp")
    
    def perform_create(self, serializer):
        salesorder = serializer.save(updated_by=self.request.user)
        handle_salesorder_order_orderitems(salesorder, **self.request.data)
        create_signature_entry(salesorder, **self.request.data)
    
    def perform_update(self, serializer):
        salesorder = serializer.save(updated_by=self.request.user)
        handle_salesorder_order_orderitems(salesorder, **self.request.data)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    
class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()

class SignatureViewSet(viewsets.ModelViewSet):
    serializer_class = SignatureSerializer
    queryset = Signature.objects.all()
    