from rest_framework import serializers
from bankapiapp.models import BankView


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankView()
        fields = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name')