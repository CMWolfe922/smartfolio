from django.forms import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    model = User

# To create a new user import the UserCreationForm from django.contrib.auth.forms
class RegisterForm(UserCreationForm):
    # Add any additional fields that I want added to the new user form
    email = forms.EmailField(required=True, unique=True, max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProgileForm(forms.ModelForm):
    # add the fields that need to be filled in for the user to be able to
    # have a profile and so that user's profile is searchable.
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    personal_email = forms.EmailField()
    work_email = forms.EmailField()
    cell_phone = forms.CharField(max_length=15)
    work_phone = forms.CharField(max_length=15)
    bio = forms.TextField(max_length=500)
    work_experience = forms.TextField(max_length=1000)
    skills = forms.ModelsChoiceField()

    class Meta:
        model = User
        fiels = ['first_name', 'last_name', 'personal_email', 'work_email', 'cell_phone', 'work_phone', 'bio', 'work_experience', 'skills']
