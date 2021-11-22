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

class Organogram(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    name           = models.CharField(max_length=250, choices=NAME_CHOICES)
    description    = models.TextField(blank = True)
    organogram_file	   = models.FileField(upload_to='organograms')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]



class ProcessFlowChart(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    name           = models.CharField(max_length=250, choices=NAME_CHOICES)
    description    = models.TextField(blank = True)
    process_chart_file   = models.FileField(upload_to='process_flow_chart')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]


class NeedsAndExpetation(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    name           = models.CharField(max_length=250, choices=NAME_CHOICES)
    description    = models.TextField(blank = True)
    needs_expetations_file   = models.FileField(upload_to='needs_expetations')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]



class ComplaintsRegister(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    name           = models.CharField(max_length=250, choices=NAME_CHOICES)
    description    = models.TextField(blank = True)
    complaints_register_file   = models.FileField(upload_to='complaints_register')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]