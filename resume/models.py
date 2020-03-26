from django.db import models

# Create your models here.
class Resume(models.Model):
    """���� ���������� "Resume"""
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title