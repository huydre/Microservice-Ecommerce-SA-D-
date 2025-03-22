from rest_framework import serializers
from .models import Customer, FullName, Address, Contact, NewCustomer, LoyaltyCustomer

class FullNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullName
        fields = ['id', 'first_name', 'middle_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'city', 'state', 'postal_code', 'country', 'is_default']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'email', 'phone_primary', 'phone_secondary', 'is_email_verified', 'is_phone_verified']

class NewCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCustomer
        fields = ['id', 'welcome_offer_used', 'registration_date']

class LoyaltyCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoyaltyCustomer
        fields = ['id', 'loyalty_points', 'tier', 'join_date']

class CustomerSerializer(serializers.ModelSerializer):
    full_name = FullNameSerializer(required=False)
    contact = ContactSerializer(required=False)
    addresses = AddressSerializer(many=True, required=False)
    customer_type = serializers.ReadOnlyField()

    class Meta:
        model = Customer
        fields = ['id', 'full_name', 'contact', 'addresses', 'date_of_birth',
                  'created_at', 'updated_at', 'customer_type']