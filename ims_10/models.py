from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings


NAME_CHOICES = (
    ("SHE", "SHE"),
    ("HR", "HR"),
    ("Finance", "Finance"),
    ("Technical Services", "Technical Services"),
    ("Reduction", "Reduction"),
    ("Engineering", "Engineering"),
    ("Security", "Security"),
    ("Other", "Other"),
)

CATEGORY_CHOICES = (
    ("Accident Investigation Reports", "Accident Investigation Reports"),
    ("Near Miss Report", "Near Miss Report"),
    ("Stop and Fix Reports", "Stop and Fix Reports"),
)

class IncidentNonConformityCorrectiveAction(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    department     = models.CharField(max_length=250, choices=NAME_CHOICES)
    name           = models.CharField(max_length=250)
    category       = models.CharField(max_length=250, choices=CATEGORY_CHOICES)
    description    = models.TextField(blank = True)
    upload_file	   = models.FileField(upload_to='ims10/all_reports')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]

