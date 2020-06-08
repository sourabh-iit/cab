from rest_framework import serialziers
from django.contrib.auth.models import User

from apps.cab.models import Driver, Cab

class UserSerializer(serialziers.ModelSerializer):
    class Meta:
        model = User
        fields = (
          'id',
          'first_name',
          'last_name',
          'username',
          'email'
        )

class CabSerialzier(serialziers.ModelSerializer):
    driver = serialziers.SerialzierMethodfield()

    def get_driver(self, cab):
        return UserSerializer(cab.driver).data

    class Meta:
        model = Cab
        fields = (
          'id',
          'cab_type',
          'curr_location',
          'number',
          'driver'
        )