from django.shortcuts import get_object_or_404, redirect, render

from .models import Professeurs

from .forms import MyFormProf, ProfessorForm



# Create your views here.
def addprof(request):
    if request.method == 'POST':
     form = MyFormProf(request.POST)
     if form.is_valid():
        form.save()
        return redirect('prof:proflist')
    else:
       form = MyFormProf() 

    return render(request, 'prof/ajouterprof.html', {'form':form})

def proflist(request):
    professeurs = Professeurs.objects.all()
    return render(request, 'prof/proflist.html', {'professeurs': professeurs})

def modifierprof(request, id):
    professeurs = get_object_or_404(Professeurs, id=id)
    if request.method == 'POST':
        form = MyFormProf(request.POST, instance=professeurs)
        if form.is_valid():
            form.save()
            return redirect('prof:proflist')
    else:
        form = MyFormProf(instance=professeurs)
    return render(request, 'utilisateurs/modifierutilisateur.html', {'form': form})

def supprimerprof(request, id):
    professeurs = get_object_or_404(Professeurs, id=id)
    professeurs.delete()
    return redirect('prof:proflist')
    

