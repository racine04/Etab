from django.shortcuts import render
from student.models.student import StudentModel
from professors.models.teacher import TeacherModel
from user.models.user import UserModel

# Create your views here.

def dashboard(request):
    # Récupérez le nombre d'élèves, de professeurs, d'utilisateurs
    nombre_eleve = StudentModel.objects.count()
    nombre_professeur = TeacherModel.objects.count()
    nombre_utilisateur = UserModel.objects.count()

    # Récupérez le nombre d'élèves par genre
    nombre_garcons = StudentModel.objects.filter(genre='M').count()
    nombre_filles = StudentModel.objects.filter(genre='F').count()

    # Passez les données au template
    context = {
        'nombre_eleve': nombre_eleve,
        'nombre_professeur': nombre_professeur,
        'nombre_utilisateur': nombre_utilisateur,
        'nombre_garcons': nombre_garcons,
        'nombre_filles': nombre_filles,
    }

    return render(request, 'dashboard.html', context)