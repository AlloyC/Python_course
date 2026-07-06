from django.contrib import admin
from .models import Profile, students, Posts, Course, Captains, Animals, JambForm, Book
# Method 1: Using a custom admin class to display specific fields and add search and filter options
class StudentAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'age', 'date')
    search_fields = ('firstname', 'lastname')
    list_filter = ('age', 'date')
    

# Method 2: using django decorators to register the model and customize the admin interface
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('student', 'experience')
    search_fields = ('student__firstname', 'student__lastname')
    list_filter = ('student__age',)

class PostsAdmin (admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ("title",)
    list_filter = ("author",)

class CaptainsAdmin(admin.ModelAdmin):
    list_display = ("title", "ship_number", "location", "long", "lat")
    search_fields = ("title", "ship_number")
    list_filter = ("location",)

class AnimalsAdmin(admin.ModelAdmin):
    list_display = ("name", "features", "can_fly")
    search_fields = ("name",)
    list_filter = ("can_fly",)

class JambFormAdmin(admin.ModelAdmin):
    list_display = ("name", "jamb_number", "email")
    search_fields = ("name", "jamb_number", "email")
    list_filter = ("school", "age")

class BookAdmin(admin.ModelAdmin):
    list_display = ("sn", "title", "subject", "genre")
    search_fields = ("title", "subject", "genre")
    list_filter = ("subject", "genre")

# Register your models here.
admin.site.register(students, StudentAdmin)
admin.site.register(Animals, AnimalsAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Course)
admin.site.register(Captains, CaptainsAdmin)
admin.site.register(JambForm, JambFormAdmin)
admin.site.register(Book, BookAdmin)


