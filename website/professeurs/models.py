from django.db import models

# Create your models here.
MATTER = [
    ('Math', 'Math'),
    ('SVT', 'SVT'),
    ('Anglais', 'Anglais'),
    ('Physique', 'Physique'),
    ('EPS', 'EPS'),
    ('Philosophie', 'Philosophie'),
    ('Francais', 'Francais'),
]

VACANT = [
    ('Oui', 'Oui'),
    ('Non', 'Non'),
]

class Professeurs(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_de_creation = models.DateField(auto_now_add=True)
    ville = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    vacant = models.CharField(max_length=50, choices= VACANT)
    age = models.PositiveIntegerField()  # Champ pour l'âge, uniquement des entiers positifs
    matiere_enseigne = models.CharField(max_length=30, choices= MATTER)
    prochain_cours = models.CharField(max_length=50)
    sujet_prochaincours = models.CharField(max_length=50)


        