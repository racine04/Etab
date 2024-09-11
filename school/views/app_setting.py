from django.shortcuts import get_object_or_404, redirect, render
from school.forms import AppSettingForm
from school.models.app_settings import AppSettingModel
from django.contrib.auth.decorators import login_required


def addsetting(request):
    
    if request.method == 'POST':
     formsetting = AppSettingForm(request.POST)
     if formsetting.is_valid():
        formsetting.save()
        return redirect('school:addschool')
    else:
       formsetting = AppSettingForm()

    app_setting= AppSettingModel.objects.all()
    if not app_setting:
        return render(request, 'setting/ajoutersetting.html', {'formsetting':formsetting})

    else :
       return redirect('school:addschool')#ajouter ecole    

@login_required(login_url='connexion:signup')
def settinglist(request):
    eleves = AppSettingModel.objects.all()
    return render(request, 'setting/settinglist.html', {'eleves': eleves})


@login_required(login_url='connexion:signup')
def modifiersetting(request, id):
    setting = get_object_or_404(AppSettingModel, id=id)
    if request.method == 'POST':
        form = AppSettingForm(request.POST, instance=setting)
        if form.is_valid():
            form.save()
            return redirect('school:listschool')
    else:
        form = AppSettingForm(instance=setting)
    return render(request, 'school/modifierschool.html', {'form': form})


def check_settings(request):
    app_setting= AppSettingModel.objects.all()
    if not app_setting:
        return redirect('school:parametre')#pour ajouter parametre

    else :
       
       return redirect('school:checkschool')#verification de l'ecole



@login_required(login_url='connexion:signup')
def supprimersetting(request, id):
    settings = get_object_or_404(AppSettingModel, id=id)
    settings.delete()
    return redirect('school:settinglist')