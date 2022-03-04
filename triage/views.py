from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import TriageForm
from .models import Triage
from django.views.generic import DetailView

def user_login(request):
    if request.user.is_authenticated:
        
        return render(request, 'home.html', get_triage())

    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {"error" : "Invalid username or password"}
            return render(request, 'login.html',context)

        login(request, user)
        return render(request, 'home.html', get_triage())

    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html', get_triage())

def get_triage():
    try:
        triage = {"triage": Triage.objects.filter(treatment=False).order_by("triage_category", "created")}
    except:
        triage = None
    return triage


@login_required
def triage(request):
    if request.method == 'POST':
        form = TriageForm(request.POST)
        if form.is_valid():
            triage = form.save(commit=False)
            triage.user = request.user
            triage.save()
            return redirect('/')
    else:
        form = TriageForm()

    return render(request, 'triage_form.html' , {'form': form})

class TriageDetail(DetailView): 
    model = Triage
    template_name = 'triage_detail.html'

@login_required
def get_under_treatment(request):
    try:
        under_treatment = {"under_treatment": Triage.objects.filter(treatment=True)}
    except:
        under_treatment = None
    return render(request, 'under_treatment.html', under_treatment)

@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request, 'logout.html')

