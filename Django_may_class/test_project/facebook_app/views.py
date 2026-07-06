from django.shortcuts import render
from .form import SignupForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def login(request):
    return render(request, 'login.html')

def signup(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'signup.html', {"form": form})

def dashboard(request):
    return render(request, 'dashboard.html')