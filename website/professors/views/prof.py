from django.shortcuts import get_object_or_404, redirect, render
from professors.forms import TeacherForm
from professors.models.teacher import  TeacherModel


def addprof(request):
    if request.method == 'POST':
     form = TeacherForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('prof:proflist')
    else:
       form = TeacherForm() 

    return render(request, 'prof/ajouterprof.html', {'form':form})

def proflist(request):
    professeurs = TeacherModel.objects.all()
    return render(request, 'prof/proflist.html', {'professeurs': professeurs})

def modifierprof(request, id):
    professeurs = get_object_or_404(TeacherModel, id=id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=professeurs)
        if form.is_valid():
            form.save()
            return redirect('prof:proflist')
    else:
        form = TeacherForm(instance=professeurs)
    return render(request, 'prof/modifierprof.html', {'form': form})

def supprimerprof(request, id):
    professeurs = get_object_or_404(TeacherModel, id=id)
    professeurs.delete()
    return redirect('prof:proflist')