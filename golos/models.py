from django.db import models
from django.contrib.auth.models import AbstractUser
import PIL

from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill
class UserD(AbstractUser):
    is_voted = models.BooleanField(default=False)
    pass


class Candidat(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True, blank=True)
    long_desc = models.CharField(max_length=300, null=True, blank=True)
    short_desc = models.CharField(max_length=40, null=True, blank=True)
    position = models.CharField(max_length=40, null=True, blank=True)
    votes = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to='candidats/', null=True, blank=True)
    photo_big = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
                                ResizeToFill(width=480,height=480)], source='img',
                               format='JPEG', options={'quality': 90})

# Create your models here.
