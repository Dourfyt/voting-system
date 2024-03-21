from django.db import models
from django.contrib.auth.models import AbstractUser

class UserD(AbstractUser):
    is_voted = models.BooleanField(default=False)
    pass


class Candidat(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    otchestvo = models.CharField(max_length=40)
    votes = models.PositiveIntegerField(default=0)


# Create your models here.
