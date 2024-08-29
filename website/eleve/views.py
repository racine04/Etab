# eleve/views.py
from django.shortcuts import get_object_or_404, redirect, render

from .models import Eleves

from .forms import MyFormStudent
 


def addeleve(request):
    if request.method == 'POST':
     form = MyFormStudent(request.POST)
     if form.is_valid():
        form.save()
        return redirect('eleve:elevelist')
    else:
       form = MyFormStudent()
    return render(request, 'eleves/ajoutereleve.html', {'form': form})

def elevelist(request):
    eleves = Eleves.objects.all()
    return render(request, 'eleves/elevelist.html', {'eleves': eleves})

def modifiereleve(request, id):
    eleves = get_object_or_404(Eleves, id=id)
    if request.method == 'POST':
        form = MyFormStudent(request.POST, instance=eleves)
        if form.is_valid():
            form.save()
            return redirect('eleve:elevelist')
    else:
        form = MyFormStudent(instance=eleves)
    return render(request, 'eleves/modifiereleve.html', {'form': form})

def supprimereleve(request, id):
    eleves = get_object_or_404(Eleves, id=id)
    eleves.delete()
    return redirect('eleve:elevelist')
