from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import TriageForm
from .models import Triage
from django.views.generic import DetailView, DeleteView

def user_login(request):
    if request.user.is_authenticated:
        
        return render(request, 'home.html', get_triage_data())

    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            context = {"error" : "Invalid username or password"}
            return render(request, 'login.html',context)

        login(request, user)
        return render(request, 'home.html', get_triage_data())

    return render(request, 'login.html')


def get_triage_data():
    triage = {"triage": Triage.objects.all()}
    return triage

@login_required
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    return render(request, 'logout.html')


@login_required
def home(request):
    return render(request, 'home.html', get_triage_data())

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

class TriageDelete(DeleteView):
    model = Triage
    template_name = 'triage_delete.html'
    success_url ="/"