from djanog.db import models
from django.contrib.auth.models import User


class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Cab(models.Model):
    TYPE1 = '0'
    TYPE2 = '1'
    CAB_TYPE_CHOICES = (
      TYPE1, 'Type 1',
      TYPE2, 'Type 2'
    )
    cab_type = models.CharField(max_length=2, choices=CAB_TYPE_CHOICES, default=TYPE1)
    number = models.CharField(max_length=50)
    # can be many to many field also
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    is_vaccant = models.BooleanField(default=False)
    curr_location = models.CharField(default="0,0")