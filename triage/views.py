from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.shortcuts import redirect, render

def user_login(request):
    if request.user.is_authenticated:
        return render(request, 'templates/home.html')

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
