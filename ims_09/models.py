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
)

CATEGORY_CHOICES = (
    ("Internal Audit Report", "Internal Audit Report"),
    ("Internal Audit Action Plans", "Internal Audit Action Plans"),
    ("External Audit Report ", "External Audit Report "),
    ("External Audit Action Plans", "External Audit Action Plans"),
)

ANALYSIS_CHOICES = (
    ("Quarterly Environmental Monitoring Report", "Quarterly Environmental Monitoring Report"),
    ("Industrial Hygiene Surveys", "Industrial Hygiene Surveys"),
)

SUB_CAT_CHOICES = (
    ("Waste management plan", "Waste management plan"),
    ("Lubricants Management Programme", "Lubricants Management Programme"),
    ("Cyanide Management Programme", "Cyanide Management Programme"),
    ("Refuse Disposal Schedule", "Refuse Disposal Schedule"),
)

class ActionPlans(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    name           = models.CharField(max_length=250)
    department     = models.CharField(max_length=250, choices=NAME_CHOICES)
    category       = models.CharField(max_length=250, choices=CATEGORY_CHOICES)
    description    = models.TextField(blank = True)
    upload_file	   = models.FileField(upload_to='ims_09/action_plans')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]



class ManagementReviewMinutes(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    name           = models.CharField(max_length=250)
    department     = models.CharField(max_length=250, choices=NAME_CHOICES)
    description    = models.TextField(blank = True)
    upload_file    = models.FileField(upload_to='ims_09/management_review_minutes')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]


class MonitoringMeasurementAnalysisPerformanceEvaluation(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    name           = models.CharField(max_length=250)
    department     = models.CharField(max_length=250, choices=NAME_CHOICES)
    category       = models.CharField(max_length=250, choices=SUB_CAT_CHOICES, blank = True)
    sub_category   = models.CharField(max_length=250, choices=ANALYSIS_CHOICES, blank = True)
    description    = models.TextField(blank = True)
    upload_file    = models.FileField(upload_to='ims_09/monitoring_measurement_analysis')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]