from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings


DEPARTMENT_CHOICES = (
    ("Other", "Other"),
    ("SHE", "SHE"),
    ("HR", "HR"),
    ("Finance", "Finance"),
    ("Technical Services", "Technical Services"),
    ("Reduction", "Reduction"),
    ("Engineering", "Engineering"),
    ("Security", "Security"),
    ("Muriel Mine", "Muriel Mine"),
)

CATEGORY_CHOICES = (
    ("Other", "Other"),
    ("Baseline Risk Assessment (BRA)", "Baseline Risk Assessment (BRA)"),
    ("Issue Based Risk Assessment", "Issue Based Risk Assessment"),
    ("Compliance Obligations Register", "Compliance Obligations Register"),
    ("IMS Objectives and targets", "IMS Objectives and targets"),
    ("ACTs", "ACTs"),
    ("Blank forms", "Blank forms"),
)

BLANK_FORM_CHOICES = (
    ("Appointmant form", "Appointmant form"),
    ("Accident form", "Accident form"),
    ("CAPEX form", "CAPEX form"),
    ("Clinic Form", "Clinic Form"),
    ("Charge form", "Charge form"),
    ("Canteen meals booking", "Canteen meals booking"),
    ("Change request form", "Change request form"),
    ("EMA form", "EMA form"),
    ("Employee Induction form", "Employee Induction form"),
    ("Evaluation", "Evaluation"),
    ("Fire extinguishers inspection form", "Fire extinguishers inspection form"),
    ("HIRA", "HIRA"),
    ("Induction manual", "Induction manual"),
    ("Inspection", "Inspection"),
    ("Indemnity form", "Indemnity form"),
    ("Near miss report form", "Near miss report form"),
    ("Petty cash", "Petty cash"),
    ("Planned Job Observation", "Planned Job Observation"),
    ("PPE Card", "PPE Card"),
    ("Release form", "Release form"),
    ("Request form", "Request form"),
    ("Stop and fix form", "Stop and fix form"),
    ("Training Register", "Training Register"),
    ("Tree cutting permit", "Tree cutting permit"),
    ("Visitor Induction form", "Visitor Induction form"),
    ("VFL", "VFL"),
)

class IMS_06_Folder(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    department     = models.CharField(max_length=250, choices=DEPARTMENT_CHOICES)
    category       = models.CharField(max_length=250, choices=CATEGORY_CHOICES)
    description    = models.TextField(blank = True)
    name           = models.CharField(max_length=250, blank = True)
    upload_file	   = models.FileField(upload_to='ims_06')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.department

    class Meta:
        ordering = ["-timestamp", "-updated"]


class BlankForm(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    department     = models.CharField(max_length=250, choices=DEPARTMENT_CHOICES)
    name           = models.CharField(max_length=250, choices=BLANK_FORM_CHOICES)
    description    = models.TextField(blank = True)
    upload_file	   = models.FileField(upload_to='ims_06/blank_forms')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]