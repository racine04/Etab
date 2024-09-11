from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from base.forms import AdressForm
from base.models.adress import AddressModel
from school.models.app_settings import AppSettingModel
from school.models.school import SchoolModel




@login_required(login_url='connexion:signup')
def addadress(request):
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting == 1:
        if count_school == 1 :    
            formadress = AdressForm()      
            if request.method == 'POST':
                formadress = AdressForm(request.POST)
                if formadress.is_valid():
                    formadress.save()
                    return redirect('adress:adresslist')
                else:
                    formadress = AdressForm() 

            return render(request, 'adress/ajouteradress.html', {'formadress':formadress})
        else:   
            return redirect('school:checkschool')
    else:
        return redirect('school:checksetting')

@login_required(login_url='connexion:signup')
def adresslist(request):
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting == 1:
        if count_school == 1 :          
            address = AddressModel.objects.all()
            return render(request, 'adress/listadress.html', {'address': address})
        else:   
            return redirect('school:checkschool')
    else:
        return redirect('school:checksetting')

@login_required(login_url='connexion:signup')
def modifieradress(request, id):
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting == 1:
        if count_school == 1 :  
            eleves = get_object_or_404(AddressModel, id=id)
            if request.method == 'POST':
                formadress = AdressForm(request.POST, instance=eleves)
                if formadress.is_valid():
                    formadress.save()
                    return redirect('adress:adresslist')
            else:
                formadress = AdressForm(instance=eleves)
            return render(request, 'adress/modifieradress.html', {'formadress': formadress})
        else:   
            return redirect('school:checkschool')
    else:
        return redirect('school:checksetting')

@login_required(login_url='connexion:signup')
def supprimeradress(request, id):
    count_app_setting = AppSettingModel.objects.count()
    count_school = SchoolModel.objects.count()
    if count_app_setting == 1:
        if count_school == 1 :          
            adress = get_object_or_404(AddressModel, id=id)
            adress.delete()
            return redirect('adress:adresslist')
        else:   
            return redirect('school:checkschool')
    else:
        return redirect('school:checksetting')