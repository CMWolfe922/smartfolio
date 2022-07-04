from email.mime import image
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from distutils.command.upload import upload
from django.dispatch import receiver
from requests import post
from django.conf import settings

# Create a NewUser class to create a custom user model. I am going to create a new user model that 
# has more base fields than the Base Django User class
class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('user email address field'), unique=True)
    username = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    about = models.TextField(_('about'), max_length=500, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(_('is user staff'), default=False)
    is_activ = models.BooleanField(default=False)
    pass


# Create a Custom user manager class. This will hold the methods for creating and saving the 
# new user models. I can also add in verifications and custom model behavior.
class CustomAccountManager(BaseUserManager):
    pass

# Portfolio Model: This is essentially the users' profile. Each user will have
# only one portfolio. Inside that portfolio they can add as many projects as
# they want, but they only get one portfolio.
class Portfolio(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# This is the Project model. Each project will be tied to a portfolio.
# The portfolio model has a many to one relationship with the project model.
# because each portfolio can have many projects. But each user can only have one
# portfolio. So the portfolio model is essentially the users profile.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, unique=True, null=True, blank=False)
    description = models.TextField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)


# This is a function that returns an image or multiple images for the
# image model.
def get_image_filename(instance, filename):
    title = instance.project.title
    slug = slugify(title)
    return settings.MEDIA_URL + "uploads/project_images/%s-%s" % (slug, filename)


# This is for loading images into a project or portfolio.
class Images(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')


# This is a function used to get project files and load them to the project.
def get_project_files(instance, filename):
    title = instance.project.title
    slug = slugify(title)
    return settings.MEDIA_URL + "uploads/project_files/%s-%s" % (slug, filename)

class Files(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_project_files, verbose_name='File')
