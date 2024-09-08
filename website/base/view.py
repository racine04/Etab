from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from base.forms import AdressForm
from base.models.adress import AddressModel




@login_required(login_url='connexion:signup')
def addadress(request):
    if request.method == 'POST':
     formadress = AdressForm(request.POST)
     if formadress.is_valid():
        formadress.save()
        return redirect('adress:adresslist')
    else:
       formadress = AdressForm() 

    return render(request, 'adress/ajouteradress.html', {'formadress':formadress})

@login_required(login_url='connexion:signup')
def adresslist(request):
    address = AddressModel.objects.all()
    return render(request, 'adress/listadress.html', {'address': address})

@login_required(login_url='connexion:signup')
def modifieradress(request, id):
    eleves = get_object_or_404(AddressModel, id=id)
    if request.method == 'POST':
        formadress = AdressForm(request.POST, instance=eleves)
        if formadress.is_valid():
            formadress.save()
            return redirect('adress:adresslist')
    else:
        formadress = AdressForm(instance=eleves)
    return render(request, 'adress/modifieradress.html', {'formadress': formadress})

@login_required(login_url='connexion:signup')
def supprimeradress(request, id):
    adress = get_object_or_404(AddressModel, id=id)
    adress.delete()
    return redirect('adress:adresslist')