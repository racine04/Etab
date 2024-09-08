from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from student.forms import StudentCardForm
from student.models.card import StudentCardModel


@login_required(login_url='connexion:signup')
def addcard(request):
    if request.method == 'POST':
     form = StudentCardForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('eleve:cardlist')
    else:
       form = StudentCardForm()
    return render(request, 'card/card.html', {'form': form})


@login_required(login_url='connexion:signup')
def cardlist(request):
    eleves = StudentCardModel.objects.all()
    return render(request, 'card/cardlist.html', {'eleves': eleves})


@login_required(login_url='connexion:signup')
def modifiercard(request, id):
    eleves = get_object_or_404(StudentCardModel, id=id)
    if request.method == 'POST':
        form = StudentCardForm(request.POST, instance=eleves)
        if form.is_valid():
            form.save()
            return redirect('eleve:cardlist')
    else:
        form = StudentCardForm(instance=eleves)
    return render(request, 'card/modifiercard.html', {'form': form})


@login_required(login_url='connexion:signup')
def supprimercard(request, id):
    eleves = get_object_or_404(StudentCardModel, id=id)
    eleves.delete()
    return redirect('eleve:cardlist')