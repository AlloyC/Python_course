from django import forms
from users.models import JambForm, Book

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class JambForms (forms.ModelForm):

    class Meta:
        model = JambForm
        fields = "__all__"
    
    
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError("You must be 18 above to submit")
        return age
    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError("Name cannot be 2 letter")
        return name
    
    def clean_jamb_number(self):
        jamb_number = self.cleaned_data['jamb_number']
        if not jamb_number.startswith("NGN"):
            raise forms.ValidationError("Invalid Jamb number")
        return jamb_number
    
# class JambForm (forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     jamb_number = forms.CharField(max_length=10)
#     school = forms.CharField(max_length=100)
#     age = forms.IntegerField()
    
#     def clean_age(self):
#         age = self.cleaned_data['age']
#         if age < 18:
#             raise forms.ValidationError("You must be 18 above to submit")
#         return age
    
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         if len(name) < 2:
#             raise forms.ValidationError("Name cannot be 2 letter")
#         return name
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["sn", "title", "subject", "genre", "image"]

    def clean_sn(self):
        sn = self.cleaned_data['sn']
        if type(sn) != "int":
            raise forms.ValidationError("Serial number must be an integer")
        return sn
