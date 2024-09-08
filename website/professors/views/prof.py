from django.shortcuts import get_object_or_404, redirect, render
from professors.forms import TeacherForm
from professors.models.teacher import  TeacherModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='connexion:signup')
def addprof(request):
    if request.method == 'POST':
     form = TeacherForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('prof:proflist')
    else:
       form = TeacherForm() 

    return render(request, 'prof/ajouterprof.html', {'form':form})

@login_required(login_url='connexion:signup')
def proflist(request):
    search_field= request.GET.get('search')
    if search_field :
        professeurs = TeacherModel.objects.filter(nom__icontains=search_field) | TeacherModel.objects.filter(prenom__icontains=search_field)
        context = {
            'professeurs': professeurs,
            'search_field':search_field,
        }
    else:    
        professeurs = TeacherModel.objects.all()
        context = {
            'professeurs': professeurs,
        }
    return render(request, 'prof/proflist.html', context)

@login_required(login_url='connexion:signup')
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

@login_required(login_url='connexion:signup')
def supprimerprof(request, id):
    professeurs = get_object_or_404(TeacherModel, id=id)
    professeurs.delete()
    return redirect('prof:proflist')