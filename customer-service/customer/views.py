from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Customer, FullName, Address, Contact, NewCustomer, LoyaltyCustomer
from .serializers import (CustomerSerializer, FullNameSerializer, AddressSerializer,
                         ContactSerializer, NewCustomerSerializer, LoyaltyCustomerSerializer)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['get'])
    def addresses(self, request, pk=None):
        customer = self.get_object()
        addresses = customer.addresses.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def add_address(self, request, pk=None):
        customer = self.get_object()
        serializer = AddressSerializer(data=request.data)

        if serializer.is_valid():
            address = serializer.save()
            customer.addresses.add(address)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def upgrade_to_loyalty(self, request, pk=None):
        customer = self.get_object()

        if hasattr(customer, 'loyalty_profile'):
            return Response({"detail": "Customer is already a loyalty member"},
                           status=status.HTTP_400_BAD_REQUEST)

        loyalty = LoyaltyCustomer.objects.create(customer=customer)
        serializer = LoyaltyCustomerSerializer(loyalty)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class FullNameViewSet(viewsets.ModelViewSet):
    queryset = FullName.objects.all()
    serializer_class = FullNameSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer