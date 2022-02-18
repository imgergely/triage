from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import TriageForm
from .models import Triage


def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')

    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {"error" : "Invalid username or password"}
            return render(request, 'login.html',context)

        login(request, user)
        return render(request, 'home.html')

    return render(request, 'login.html')


@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request, 'logout.html')

@login_required
def user_register(request):
    return render(request, 'register.html',{})

@login_required
def home(request):
    triage = {"triage": Triage.objects.all()}
    return render(request, 'home.html', triage)

@login_required
def triage(request):
    if request.method == 'POST':
        form = TriageForm(request.POST)
        if form.is_valid():
            
            return redirect('/triage_form/')
    else:
        form = TriageForm()

    return render(request, 'triage_form.html' , {'form': form})