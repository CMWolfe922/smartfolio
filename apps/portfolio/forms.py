from django.forms import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    model = User

# To create a new user import the UserCreationForm from django.contrib.auth.forms
class RegisterForm(UserCreationForm):
    # Add any additional fields that I want added to the new user form
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
        fields = ['username', 'email', 'password1', 'password2']
