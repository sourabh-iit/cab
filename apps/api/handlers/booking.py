from rest_framework import APIView
from rest_framework.http import Response
from rest_framework.exceptions  import ValidationError, PermissionDenied

from apps.cab.models import Customer, Cab
from apps.api.serializers.cab import CabSerialzier


class CabBookingHandler(APIView):
    def post(self, request, cab_type):
        user_location = request.data.get('location', '')
        cabs = Cab.objects.filter(cab_type=cab_type, is_vaccant=True)
        cab = self.getNearestCab(user_location, cabs)
        # send notification to cab driver about booking
        serialzier = CabSerialzier(cab)
        return Response(serialzier.data)

    def getNearestCab(self, user_location, cabs):
        # logic to compute nearest cab from user location
        if user_location=='':
            raise ValidationError('Invalid user location')
        return cabs.first()


class CabsHandler(APIView):
    def get(self, request, cab_type):
        data = request.data
        cabs = self.getNearCabs(cab_type, data.get('location', ''))
        serialzier = CabSerialzier(cabs, many=True)
        return Response(serialzier.data)

    def getNearCabs(self, cab_type, user_location):
        # logic to get near cabs from user location
        try:
            latitude, longitude = user_location.split(',')
        except Exception:
            raise ValidationError('Invalid user location provided')
        cabs = Cab.objects.filter(cab_type=cab_type, is_vaccant=True)
        return cabs