from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from distutils.command.upload import upload
from django.dispatch import receiver
from requests import post
from django.conf import settings

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=500)

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, unique=True, null=True, blank=False)
    description = models.TextField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

def get_image_filename(instance, filename):
    title = instance.project.title
    slug = slugify(title)
    return settings.MEDIA_URL + "uploads/project_images/%s-%s" % (slug, filename)

class Images(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')

def get_project_files(instance, filename):
    title = instance.project.title
    slug = slugify(title)
    return settings.MEDIA_URL + "uploads/project_files/%s-%s" % (slug, filename)

class Files(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_project_files, verbose_name='File')
