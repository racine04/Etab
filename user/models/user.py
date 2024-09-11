from django.db import models

from base.models.helpers.datemodel import DateTimeModel
from school.models.school import SchoolModel



from .role_user import RoleUserModel

# Create your models here.
class UserModel(DateTimeModel):
    pseudo = models.CharField(max_length=10, unique= True)
    mot_de_passe = models.CharField(max_length=128)
    date_de_creation = models.DateField(auto_now_add=True)
    role = models.ManyToManyField(RoleUserModel)
    school = models.ForeignKey(SchoolModel, on_delete=models.CASCADE, null=True, blank=True)



    def __str__(self):
        return self.pseudo
    
