from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text