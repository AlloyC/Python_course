from django.db import models
from django.contrib.auth.models import User

# User.objects.create_user(username='wilson', password='123567')

# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=7)
    course_title = models.CharField(max_length=50)

    def __str__(self):
        return self.course_code
    
    

class students(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    bio = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    courses_enrolled = models.ManyToManyField(Course, related_name='enrolled_students')

    class Meta:
        verbose_name = "students"
        verbose_name_plural = "students"
 
    def __str__(self):
        return self.firstname



class Profile(models.Model):
    student = models.OneToOneField(students, on_delete=models.CASCADE, related_name='profile')
    experience = models.TextField()

    def __str__(self):
        return f"{self.student}'s Profile"


class Posts(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(students, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "posts"
        verbose_name_plural = "posts"


class Captains(models.Model):
    title = models.CharField(max_length=250)
    ship_number = models.IntegerField()
    location = models.CharField(max_length=250)
    lat = models.FloatField()
    long = models.FloatField()

    class Meta:
        verbose_name = "captains"
        verbose_name_plural = "captains"

    def __str__(self):
        return self.title
    
# Model name Animals
# add to admin 
# fields name, features and can_fly (boolean)
# create a view
# create a url with /animals endpoint

class Animals(models.Model):
    name = models.CharField(max_length=255)
    features = models.TextField()
    can_fly = models.BooleanField()

    class Meta:
        verbose_name = "animals"
        verbose_name_plural = "animals"

    def __str__(self):
        return self.name
    
class JambForm (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    jamb_number = models.CharField(max_length=10)
    school = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Book(models.Model):
    sn = models.IntegerField()
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Books")
    reviewed = models.BooleanField(default=False)
    # author = models.ForeignKey(students, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title