from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse as HR
from users.models import students, Animals, JambForm as JambDB, Book
import random
from .forms import ContactForm, JambForms as JambForm, BookForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def recent(request):
    student = students.objects.select_related('profile').prefetch_related('posts')
    return render(request, 'index.html', {'student': student})

def contact(request):
    name = ["Samuel", "abby", "Isreal", "Peter", "Daniel"]
    context = {
        "name" : random.choice(name)
    }
    return render(request, "Details/contact_us.html", context)

class AboutView(View):
    def get(self, request):
        return render(request, "Details/about_us.html")

def animals(request):
    animals = Animals.objects.all()
    context = {
        "animals" : animals
    }
    return render(request, "details/animal.html", context)

def paid(request):
    return HR("This the paid products")

def homePageOne(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"Alert!!!, {name} with email {email} just sent the message {message}")

    return render(request, "home.html")

def homePageTwo(request):
    form = ContactForm()
    context = {
        "form" : form
    }
    return render(request, "home1.html", context)

def homePageThree(request):
    form = JambForm()
    if request.method == "POST":
        form = JambForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data['name']
            # email = form.cleaned_data['email']
            # jamb_number = form.cleaned_data['jamb_number']
            # school = form.cleaned_data['school']
            # age = form.cleaned_data['age']
            # jambData = JambDB(
            #     name = name, email = email, jamb_number = jamb_number, school = school, age = age
            # )
            # jambData.save()
            # print(f"Hello Admin,\nThe user {name} just submitted! \nContent: \n  Name: {name}\n  Email: {email} \n  Jamb Number: {jamb_number} \n  School: {school} \n  Age: {age} \nPlease respond to them ASAP!")

    context = {
        "form" : form
    }
    return render(request, "home2.html", context)

def homePageFive(request):
    return render(request, "home5.html")

def correction(request):
    return render(request, "correction.html")

def library(request):
    form = BookForm()
    book = Book.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {
        "form" : form,
        "books" : book
    }

    return render(request, "library.html", context)

def signup(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'signup.html', {"form": form})

def login(request):
    form = AuthenticationForm
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home1')
            
    return render(request, 'login.html', {"form": form})

def logout(request):
    auth_logout(request)
    return redirect("/products/login")

def dashboard(request):
    return render(request, 'dashboard.html')