from django.db import models

from base.models.helpers.namemodel import NamedDateTimeModel

# Create your models here.
class RoleUserModel(NamedDateTimeModel):
    role_user= models.CharField(max_length=100)

    def __str__(self):
        return self.role_user