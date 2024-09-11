from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from school.models.app_settings import AppSettingModel
from school.models.school import SchoolModel
from student.models.student import StudentModel
from professors.models.teacher import TeacherModel
from user.models.user import UserModel

# Create your views here.
@login_required(login_url='connexion:signup')
def dashboard(request):
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting == 1:
        if count_school == 1 :  
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
        else:   
            return redirect('school:checkschool')
    else:
        return redirect('school:checksetting')