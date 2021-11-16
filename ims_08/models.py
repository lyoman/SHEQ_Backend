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
    ("Standard Task Procedures", "Standard Task Procedures"),
    ("Inspections", "Inspections"),
    ("PJO and VFL", "PJO and VFL"),
)

MANAGEMENT_CHOICES = (
    ("Management of Change", "Management of Change"),
    ("Contractor Management", "Contractor Management"),
    ("Emergency preparedness and response", "Emergency preparedness and response"),
    ("Mock Drill Schedules, Reports and Action Plans", "Mock Drill Schedules, Reports and Action Plans"),
    ("Register of emergency equipment ", "Register of emergency equipment "),
    ("Audits, Inspections of emergency equipment", "Audits, Inspections of emergency equipment"),
    ("Other", "Other"),
)

class OperationalPlanningControl(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    department     = models.CharField(max_length=250, choices=NAME_CHOICES)
    name           = models.CharField(max_length=250)
    category       = models.CharField(max_length=250, choices=CATEGORY_CHOICES)
    description    = models.TextField(blank = True)
    upload_file	   = models.FileField(upload_to='ims08/operational_planning_control')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]



class ManagementDocuemnts(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    name           = models.CharField(max_length=250)
    category       = models.CharField(max_length=250, choices=MANAGEMENT_CHOICES)
    description    = models.TextField(blank = True)
    upload_file   = models.FileField(upload_to='ims08/management_documents')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]

