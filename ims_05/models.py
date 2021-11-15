from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings


DEPARTMENT_CHOICES = (
    ("SHE", "SHE"),
    ("HR", "HR"),
    ("Finance", "Finance"),
    ("Technical Services", "Technical Services"),
    ("Reduction", "Reduction"),
    ("Engineering", "Engineering"),
    ("Security", "Security"),
)

CATEGORY_CHOICES = (
    ("Legal and IMS appointments", "Legal and IMS appointments"),
    ("SHE Policy", "SHE Policy"),
    ("Consultation and participation", "Consultation and participation"),
)

class IMS05_Folder(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    department     = models.CharField(max_length=250, choices=DEPARTMENT_CHOICES)
    category      = models.CharField(max_length=250, choices=CATEGORY_CHOICES)
    description    = models.TextField(blank = True)
    upload_file	   = models.FileField(upload_to='ims_05')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.department

    class Meta:
        ordering = ["-timestamp", "-updated"]