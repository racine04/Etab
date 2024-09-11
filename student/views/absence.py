from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from student.forms import AbsenceForm
from student.models.absence import AbsenceModel


@login_required(login_url='connexion:signup')
def addabsence(request):
    if request.method == 'POST':
     form = AbsenceForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('eleve:absencelist')
    else:
       form = AbsenceForm()
    return render(request, 'absence/ajouterabsence.html', {'form': form})


@login_required(login_url='connexion:signup')
def absencelist(request):
    eleves = AbsenceModel.objects.all()
    return render(request, 'absence/absencelist.html', {'eleves': eleves})


@login_required(login_url='connexion:signup')
def modifierabsence(request, id):
    eleves = get_object_or_404(AbsenceModel, id=id)
    if request.method == 'POST':
        form = AbsenceForm(request.POST, instance=eleves)
        if form.is_valid():
            form.save()
            return redirect('eleve:elevelist')
    else:
        form = AbsenceForm(instance=eleves)
    return render(request, 'absence/modifierabsence.html', {'form': form})


@login_required(login_url='connexion:signup')
def supprimerabsence(request, id):
    eleves = get_object_or_404(AbsenceModel, id=id)
    eleves.delete()
    return redirect('eleve:absencelist')