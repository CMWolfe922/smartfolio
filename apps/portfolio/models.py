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
class Project(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=120, required=True, unique=True)
    description = models.TextField()

def get_image_filename(instance, filename):
    title = instance.project.title
    slug = slugify(title)
    return settings.MEDIA_URL + "uploads/project_images/%s-%s" % (slug, filename)

class Images(models.Model):
    project = models.ForeignKey(Project, default=None)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')
