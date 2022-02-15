from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from formtools.wizard.views import SessionWizardView
from .forms import TriageAForm, TriageBForm


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
    return render(request, 'home.html')

class TriageWizard(SessionWizardView):
    template_name = "triage_form.html"
    form_list = [TriageAForm, TriageBForm]
    def done(self, form_list, **kwargs):
        print(form.cleaned_data for form in form_list)

        #return render(self.request, 'triage_web_app/done.html', {
        #    'form_data': [form.cleaned_data for form in form_list],
        #})