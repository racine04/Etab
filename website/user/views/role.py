from django.shortcuts import get_object_or_404, redirect, render
from user.forms import RoleUserForm
from user.models.role_user import RoleUserModel


def addrole(request):
    if request.method == 'POST':
     formrole = RoleUserForm(request.POST)
     if formrole.is_valid():
        formrole.save()
        return redirect('utilisateur:listrole')
    else:
       formrole = RoleUserForm() 

    return render(request, 'role/ajouterrole.html', {'formrole':formrole})

def rolelist(request):
    roles = RoleUserModel.objects.all()
    return render(request, 'role/listrole.html', {'roles': roles})

def modifierrole(request, id):
    role = get_object_or_404(RoleUserForm, id=id)
    if request.method == 'POST':
        form = RoleUserForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('utilisateur:listrole')
    else:
        form = RoleUserForm(instance=role)
    return render(request, 'role/modifierrole.html', {'form': form})

def supprimerrole(request, id):
    role = get_object_or_404(RoleUserModel, id=id)
    role.delete()
    return redirect('utilisateur:listrole')