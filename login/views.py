from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm

from school.models.app_settings import AppSettingModel
from school.models.school import SchoolModel

# Create your views here.
def signup(request):
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting == 1:
        if count_school == 1 :  
            if request.user.is_authenticated:
                return redirect('dashboard:dashboard')

            if request.method == 'POST':
                username = request.POST.get('identifiant')
                password = request.POST.get('password')
                
                # Vérification des champs
                if not username or not password:
                    return render(request, 'login/signup.html', {'error': 'Veuillez remplir tous les champs.'})
                
                # Création de l'utilisateur
                user = User(username=username)
                user.set_password(password)
                user.save()
                
                # Connexion de l'utilisateur après l'inscription
                login(request, user)
                return redirect('dashboard:dashboard')
            
            return render(request, 'login/signup.html')
        else:   
            return redirect('school:checkschool')
    else:
        return redirect('school:checksetting')

def login_view(request):
    # Si l'utilisateur est déjà connecté, le rediriger vers le tableau de bord
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting == 1:
        if count_school == 1 :      
            if request.user.is_authenticated:
                return redirect('dashboard:dashboard')

            # Traitement du formulaire de connexion
            if request.method == 'POST':
                form = AuthenticationForm(request, data=request.POST)
                if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    return redirect('dashboard:dashboard')
            else:
                form = AuthenticationForm()

            return render(request, 'login/signin.html', {'form': form})

        else:   
            return redirect('school:checkschool')
    else:
        return redirect('school:checksetting')

def checklogin(request):
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting == 1:
        if count_school == 1 :      
            # Vérifier si l'utilisateur est déjà connecté
            if request.user.is_authenticated:
                return redirect('dashboard:dashboard')
            else:
                return redirect('connexion:signin')
        else:   
            return redirect('school:checkschool')
    else:
        return redirect('school:checksetting')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('connexion:signin')
    return redirect('connexion:signin')