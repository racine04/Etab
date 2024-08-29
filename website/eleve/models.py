from django.db import models

# Définir la liste des classes avant la déclaration de la classe Eleves
CLASSES = [
    ('Tle', 'Terminale'),
    ('1ere', 'Première'),
    ('2nd', 'Deuxième'),
    ('3eme', 'Troisième'),
    ('4eme', 'Quatrième'),
    ('5eme', 'Cinquième'),
    ('6eme', 'Sixième'),
]

GENDER = [
    ('M', 'Masculin'),
    ('F', 'Féminin'),
    
]

class Eleves(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_de_creation = models.DateField(auto_now_add=True)
    ville = models.CharField(max_length=50)
    telephone = models.CharField(max_length=50)
    age = models.PositiveIntegerField()  # Champ pour l'âge, uniquement des entiers positifs
    genre = models.CharField(max_length=10, choices=GENDER) 
    classe = models.CharField(max_length=10, choices=CLASSES)  # Liste à choix unique
    matricule = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nom} {self.prenom}"
