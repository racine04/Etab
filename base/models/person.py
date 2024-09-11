from django.db import models

from user.models.user import UserModel
from base.models.adress import AddressModel
from ..models.helpers.datemodel import DateTimeModel


GENDER = [
    ('F', 'WOMEN'),
    ('M', 'MEN'),
    ('O', 'OTHER'),
]

class Person(DateTimeModel):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_de_creation = models.DateField(auto_now_add=True)
    picture = models.URLField()
    telephone = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, choices= GENDER)
    age = models.PositiveIntegerField()  # Champ pour l'âge, uniquement des entiers positifs
    adress = models.OneToOneField(AddressModel, on_delete=models.CASCADE)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    
    class Meta:
        abstract= True