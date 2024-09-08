from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
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

def login_view(request):
    # Si l'utilisateur est déjà connecté, le rediriger vers le tableau de bord
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

def checklogin(request):
    # Vérifier si l'utilisateur est déjà connecté
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    else:
        return redirect('connexion:signup')
