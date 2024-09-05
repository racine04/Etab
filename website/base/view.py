from django.shortcuts import get_object_or_404, redirect, render

from base.forms import AdressForm
from base.models.adress import AddressModel





def addadress(request):
    if request.method == 'POST':
     formadress = AdressForm(request.POST)
     if formadress.is_valid():
        formadress.save()
        return redirect('adress:adresslist')
    else:
       formadress = AdressForm() 

    return render(request, 'adress/ajouteradress.html', {'formadress':formadress})

def adresslist(request):
    address = AddressModel.objects.all()
    return render(request, 'adress/listadress.html', {'address': address})

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

def supprimeradress(request, id):
    adress = get_object_or_404(AddressModel, id=id)
    adress.delete()
    return redirect('adress:adresslist')