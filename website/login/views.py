from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['identifiant']
        password = request.POST['password']
        if not username or not password:
            return render (request, 'login/signup.html')
        user = User(username=username)
        user.save()
        user.password = password
        user.set_password(user.password)
        user.save()
        login(request, user)
        return redirect('dashboard:dashboard')

    return render(request, 'login/signup.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login/signin.html', {'form': form})

