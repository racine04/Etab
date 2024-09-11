from django.db import models

from ..models.helpers.namemodel import NamedDateTimeModel



# Create your models here.

class AddressModel(NamedDateTimeModel):
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.country}"