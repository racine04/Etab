from django.db import models

# Create your models here.
class Utilisateurs(models.Model):
    pseudo = models.CharField(max_length=10, unique= True)
    mot_de_passe = models.CharField(max_length=128)
    date_de_creation = models.DateField(auto_now_add=True)
