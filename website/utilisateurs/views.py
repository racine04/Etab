from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Utilisateurs

from .forms import MyForm


# Create your views here.

def addutilisateur(request):
    if request.method == 'POST':
        username = request.POST['identifiant']
        password = request.POST['password']
        if not username or not password:
            return render (request, 'utilisateurs/ajouterutilisateur.html')
        user = User(username=username)
        user.save()
        user.password = password
        user.set_password(user.password)
        user.save()
        login(request, user)
        return redirect('utilisateur:listutilisateur')

    return render(request, 'utilisateurs/ajouterutilisateur.html')

def utilisateurlist(request):
    utilisateurs = User.objects.all()
    return render(request, 'utilisateurs/listutilisateur.html', {'utilisateurs': utilisateurs})

def modifierutilisateur(request, id):
    utilisateur = get_object_or_404(Utilisateurs, id=id)
    if request.method == 'POST':
        form = MyForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('utilisateur:listutilisateur')
    else:
        form = MyForm(instance=utilisateur)
    return render(request, 'utilisateurs/modifierutilisateur.html', {'form': form})

def supprimerutilisateur(request, id):
    utilisateur = get_object_or_404(Utilisateurs, id=id)
    utilisateur.delete()
    return redirect('utilisateur:listutilisateur')
    