## Introduction

- Django is a python framework the make it easy to create web apis and website using
- it comes with boilerplate that makes it easy to create web applications

## Type of python framework

- Flask - lightweight application framework
- Django - robust framework
- fastAPI - for developing APIs
- sqlachedemy - datascience

### Other python frameworks

- openml
- tinyml
- NLP
- Tensorflow & TFlite

## How it works

- It works based on MVTU design principles
- M - MODEL: Django model provides data from the database using Object Relational Mapping ORM. ORM makes it easy to work with database. It must be written in a file called models.py
- V - VIEW: It is a method or function that uses http request as argument to fetch data from the models to the templates, or import the relevant models needed and send the requested data to the template. they are written in views.py. types of request or HTTP method are GET POST PUT PATCH and DELETE
- T - TEMPLATES: This is the file where you describe the result to be represented. They are often html file and saved in a template folder
- U - URLs: Django provides a way to navigate between different template. The configuration is done in the urls.py file. It helps you to decorate a template file to a standard url endpoint

- It also comes with sqlite3 database which is not suitable for production because it is temporary database

## How to set up venv [global pc]

- Go to cmd and type "pip install virtualenv"
- pip is a package manager in python that enables you install libraries
- Every project requires that you create a virtual environment before you begin to develop

## Creating your venv in your project

- type "virtualenv [name of virtual env (venv)]"
- Option 2: type "python -m venv venv"

## To activate

- type "venv\Scripts\activate" in your terminal

## In production mode

- always follow the production guidelines

## Others information

- cpanel is used for hosting wordpress website

## Python files

- init.py: it initializes the code. it is like a constructor
- asgi: asynchronous server gateway. It allows your django application to handle async features eg: async views, live notification etc.
- wsgi: web server gateway interface. It is used for traditional synchronous web applications

## Creating and running a django application

- venv/Scripts/activate -- start your virtual enviroment
- pip install django -- install django
- django-admin startproject <name of project> -- start your django project
- python manage.py startapp users -- create apps. App is a web application in your project that has specific meaning
- create a urls.py file in the users app (in the app you just created).
- in urls.py
  ""
  from django.contrib import admin
  from django.urls import include, path

  urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('users.urls')) # your app folder.urls
  ]
  ""

- in app/views.py {from django.http import HttpResponse as HR}
- In the main project app, inside TEMPLATES, 'DIRS': [BASE_DIR / 'templates'],
- create your models then migrate them === python manage.py makemigrations > python manage.py migrate
- create the superuser === python manage.py createsuperuser
- register the models in the admin.py file

## other commands for manage

- python manage.py makemigrations - to make migration
- python manage.py migrate - to migrate model
- python manage.py createsuperuser
- python manage.py collectstatic
- python manage.py shell

## Assignment

Create a tictactoe game with python.

- show welcome to my tictactoe game
- select position
- x show be purple color and o should be yellow color

find the library to change color

compare 6 difference between flask Django and FastAPI

- Check what social media is using them

How to use python manage.py shell to insert, update and delete database values
MAY 25

- Study many to many relationship and implememnt it on the current projects we have using the model "Course". A student should be able to add more than one course
- Create a django project that uses all model reationships the project should be fresh and should be a blog projects where different users can post on different topics.

- Figure out a way to remove the extra "s" in the admin
- in tabular form list 5 difference between sqlite, mongodb and postgresql

June 5

- Create a 5 pages website
- Downlaoad a template
- Render the navbar, footer from the base file
- link all pages in navbar with django links
- serve all images as styles using django

## Classwork

- create a new app called products
- add 3 views with any name of your choice
- create urls for each view
- create a corresponding url.py with urls for the views you created
- serve them

- create an app called facebook_app
- create 3 templates files for login resister and dashboard
- create 3 views and url that renders each page
- clone webpages with resourcesaver.

May 21
In django, database tables are created in objects called models.

- To run multiple projects servers run {python manage.py runserver <port number: 0.0.1:8001>}
- When making a new model always start with Capital letter
- Django comes with a boilerplate admin dashboard. You can create an admin user with the command {python manage.py createsuperuser}.
- Add in the values for the form given and your admin will be created successfully.
  First of all, before attempting to migrate model, you must first add the app that contains the model to settings.py
  next, make migration {python manage.py makemigrations}, then migrate {python manage.py migrate} finally register your model in the admin.py. This will migrate the model tables to DB.

May 25
django has different model fields:
| model field | Use | value type |
|-------------|-------------------------------------|----------------|
| CharField | Charfield(max_length= 20) | text |
| IntegerField | IntergerField() | numbers |
| TextField | TextField() | long text |
| BooleanField | BooleanField() | True or False |
| DateTimeField | DatetimeField(auto_now_add = True) | date and time |
| DecimalField | DecimalField(max_digits=10, decimal_places=2) | decimal number |
| EmailField | EmailField(max_length=255) | email text |
| ImageField | ImageField(upload_to='images/') | Image upload |
| FileField | FileField(upload_to='') | Files upload |
| FloatField | FloatField(max_length=10) | floating point numbers |
| JSONField | JSONField() | JSON data |

## Model Relationship in Django

- One-to-one relationships one object belongs to exactly one object. E.g One user has only one profile
- One-to-many (ForeignKey) relationships one object to many related objects. E.g One author multiple post
- Many to mamy relationship many object to many related objects. E.g one student many courses

## Djago string representation

It is importatnt to add a string representation to your model. It helps the admin use the specified nam needed instead of the object itself.

May 28

# Admin.py

In admin.py, you register models that have be created in models.oy so they can show in the admin in interface

- first your import the model
- register it with admin.site.register(The Model)
- Note that its not all models should be registered in the admin. In the admin your can also write functions that influences the behaviours of the model you registered.
- There a django boiler plate attribute called ModelAdmin that allows you to customize the django admin model using different fields attributes. You do this by creating a class with admin.ModelAdmin argument

```

          class StudentAdmin(admin.ModelAdmin):
          list_display = ('firstname', 'lastname', 'age', 'date')
          search_fields = ('firstname', 'lastname')
          list_filter = ('age', 'date')

          admin.site.register(student, StudentAdmin)

```

you can also use a django decorator by writing @ just before the model to be registered.

```

        @admin.register(student)

```

## Comparison: sqlite, mongodb and postgresql

| Feature                    | SQLite                                       | MongoDB                                  | PostgreSQL                                     |
| -------------------------- | -------------------------------------------- | ---------------------------------------- | ---------------------------------------------- |
| Data model                 | Relational, stored as a single file          | Document store (JSON-like documents)     | Relational, full-featured SQL database         |
| Schema                     | Simple / light (good for prototypes)         | Flexible, schema-less (easy to change)   | Structured, migrations and strong types        |
| Query language             | Basic SQL for simple queries                 | JSON-style queries and aggregations      | Full SQL with joins, window functions          |
| Transactions & concurrency | ACID but limited for heavy concurrent writes | Supports transactions; built for scaling | Strong ACID support and high concurrency       |
| Typical use                | Local dev, small apps, testing               | Scale-out apps, flexible data, rapid dev | Production systems, analytics, complex queries |

## DJANGO VIEW

It is a view that contains the logic that controes what the users see. example, a url, kvrl.com, the endpoint will call the view corresponding to the endpoint, the view gets the response and send data to the template. Type of views are function-base, FVB, and class-based views, CBV.

#### Function-based view

- It is beginner friendly
- It has simple syntax
- It is very repitive
- It is harder to scale in large project

```

      from django.shortcuts import render
      from users.models import students, Posts

      def recent(request):
      student = students.objects.select_related('profile').prefetch_related('posts')
      return render(request, 'index.html', {'student': student})

```

#### Class-based view

- It uses python classes instead of functions
- It is not repitive
- the .as_view() method converts a class into a callable view
- It is more advanced and used for large scale app
- It is reuseable

```

<!-- In the view.py file -->

        from django.shortcuts import render
        from django.views import View

        class AboutView(View):
            def get(self, request):
                return render(request, "Details/about_us.html")

<!-- In the urls.py file -->

        from django.urls import path
        from .views import AboutView

        urlpatterns = [
            path('about_us', AboutView.as_view(), name="about_us")
        ]

```

### URL routing connects urls to views

- URL routing connects urls to views. e.g path('contact', viewfunction/viewClass, name="contact")
- for dynamic url, path("products/<<pk:token>>/",view.productdetails, name="productdetail"),
- - <<pk:>> - tokens endpoint
- - <<str:>> - string endpoint
- - <<int:>> - interger, id endpoint
- - <<slug:>> - slug endpoint

### Context variable

- It is a dictionay variable for passing model(s) data to the template.
- It is a cleaner way to organize all models to be passed to the template.

## Templates

- templates are html files django renders
- the html files are stored in the templet folders
- to set up your template folder go to your settings file and type

```

      TEMPLATES, 'DIRS': [BASE_DIR / 'templates'],

```

- To pass the context variabel value in the template django utilizes curly bracket `{{ }}`

### Template loop

- It is simply writing for loops or anyother loop in your templates.
- It is done by using `{% %}`
- example

```

  {% for post in posts %}
    content
  {% endfor %}

```

### Template inheritance

- This is a base html file created to house repeated content over series of pages.
- It makes use of `{% block title%}`, `{% endblock %}` and `{% block content %}` as placeholders for the variable templates

### Inheritance is important

- Easier maintenance
- cleaner code
- Reuseable

### Template including

- Create a template for another set of code and including it into the main code.
- Example creating a footer.html file and including it in your base.html

## Static Files

- They are files that don't change dynamically eg css, images and js
- They are done inside a folder called Static in your root folder

```
<!-- In settings.py -->

  STATIC_URL = 'static/'
  STATICFILES_DIRS = [
    BASE_DIR / "static",
  ]

<!-- in template files using the static files -->
  {% load static %}

  <!-- To use static css file -->
    <link rel="stylesheet" href="{% static 'css/correctionstyle.css' %}">

  <!-- To use static image file -->
    <img src="{% static 'images/esp32.png' %}" width="100%" alt="esp32">
```

## Pages linking (URL)

- The url of a page in the template html file is the path name of the page and not the actual url

```
<!-- In the project urls.py file -->
  from django.conf import settings
  from django.conf.urls.static import static

  <!-- After the urlpatterns -->
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #needed for the media file url to display correctly

<!-- In the template file that needs the url -->
  <a class="navbar-brand" href="{% url 'home1' %}">Sky.com</a>
```

## Media files

- Django media files used to store multimedia data uploaded to the database.
- The media folder is automatically created when we upload a new media file to our database.
- To all this functionality, we have to:

```
<!-- In settings.py file -->
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media' #manually added
```

- - then `pip install pillow` to make use if models.ImageField(upload_to).
- - Finally update your model to allow image upload.

## Django forms
- A form allows user send data to your application. Example include: contact form registration form blog submission form
- Cross-Site Request Forgery (CSRF) token is required to use django forms

### form flow
--------------------

```

User flls form
      |
Browser sends data
      |
Django recieves request
      |
Validation
      |
Save to DB
      |
Response returned

```

## CSRF Protection
- Cross-Site Request Forgery (CSRF) is security attack where another site tries to submit forms onbehalf of another user
- without csfr, django throws 403 forbbiden error meaning csrf verificaton failed

## Authentication and Authorization Guide

Brief note: this guide is based on the auth-related views in [test_project/products/views.py](test_project/products/views.py). The file already handles signup, login, and logout, but the `dashboard` view is still open to everyone, so authorization still needs to be applied there.

### Authentication

Authentication answers the question, "Who is the user?" In Django, the built-in forms and session helpers make this simple.

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
```

#### Signup view

`UserCreationForm` creates a new user account. In the current view file, the form is displayed on GET and saved on POST when it is valid.

```python
def signup(request):
  form = UserCreationForm
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
  return render(request, 'signup.html', {"form": form})
```

#### Login view

`AuthenticationForm` checks the username and password. After validation, `form.get_user()` returns the authenticated user, and `auth_login()` stores the user in the session.

```python
def login(request):
  form = AuthenticationForm
  if request.method == "POST":
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      auth_login(request, user)
      return redirect('home1')

  return render(request, 'login.html', {"form": form})
```

#### Logout view

`auth_logout()` removes the current user from the session, then redirects them to the login page.

```python
def logout(request):
  auth_logout(request)
  return redirect("/products/login")
```

### Authorization

Authorization answers the question, "What is the user allowed to do?" Authentication alone is not enough for private pages. For example, the current `dashboard` view returns a template without checking whether the user is logged in.

Use `login_required` to protect a view that should only be visible to authenticated users.

```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/products/login')
def dashboard(request):
  return render(request, 'dashboard.html')
```

Use permissions or group checks when different users should see different content.

```python
from django.contrib.auth.decorators import user_passes_test

def is_staff_user(user):
  return user.is_staff

@user_passes_test(is_staff_user)
def admin_panel(request):
  return render(request, 'admin_panel.html')
```

### Typical flow

1. User opens the signup page and creates an account.
2. User submits the login form with valid credentials.
3. Django authenticates the user and creates a session.
4. Protected pages check whether the session belongs to a logged-in user.
5. Logout clears the session and sends the user back to the login page.

### Key ideas to remember

- Authentication confirms identity.
- Authorization controls access.
- `UserCreationForm` is for registration.
- `AuthenticationForm` is for login.
- `auth_login()` and `auth_logout()` manage the session.
- `login_required` is the simplest way to protect a page.
- Role-based access can be handled with `user_passes_test`, permissions, or groups.

June 18

- Form validation
- cleaned form
- form error display
- submit form to admin
- modelForm
- Django validate a form by using ```form.is_valid()``` method.
- custom form validation - note that the function name clean_< your name choice >. ```clean``` is a keyword that must be used for your custom form validation.

```
if request.method == "POST":
    form = JambForm(request.POST)
    <!-- form validation -->
    if form.is_valid():
      <!-- cleaned form data  -->
      print(form.cleaned_data)

      <!-- Custom validation -->
      <!-- In thte class for the form -->
      def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("You must be 18 above to submit")
        return age
```


## Authentication & Authorizations
- Authentication anwers the question "who are you?"
- Authorisation answers "what am I allowed to do?"
- Django comes with inbuilt user model. The models comes with uersname, email, password, first_name, last_name
- Django has a boilerplate user creation form. To utilize the form simply import user creation form
```
  from django.contrib.auth.forms import UserCreationForm
```

- There are 2 ways to implement the login form in django
- The first way is using the authenticate property
- The second way is using the authentication form