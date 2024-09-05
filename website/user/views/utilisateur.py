from django.shortcuts import get_object_or_404, redirect, render

from ..models.user import UserModel

from ..forms import MyUserForm


def addutilisateur(request):
    if request.method == 'POST':
     form = MyUserForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('utilisateur:listutilisateur')
    else:
       form = MyUserForm() 

    return render(request, 'utilisateurs/ajouterutilisateur.html', {'form':form})

def utilisateurlist(request):
    search_field= request.GET.get('search')
    if search_field :
        utilisateurs = UserModel.objects.filter(pseudo__icontains=search_field)
        context = {
            'utilisateurs': utilisateurs,
            'search_field':search_field,
        }
    else:    
        utilisateurs = UserModel.objects.all()
        context = {
            'utilisateurs': utilisateurs,
        }
             
    return render(request, 'utilisateurs/listutilisateur.html', context)

def modifierutilisateur(request, id):
    utilisateur = get_object_or_404(UserModel, id=id)
    if request.method == 'POST':
        form = MyUserForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('utilisateur:listutilisateur')
    else:
        form = MyUserForm(instance=utilisateur)
    return render(request, 'utilisateurs/modifierutilisateur.html', {'form': form})

def supprimerutilisateur(request, id):
    utilisateur = get_object_or_404(UserModel, id=id)
    utilisateur.delete()
    return redirect('utilisateur:listutilisateur')