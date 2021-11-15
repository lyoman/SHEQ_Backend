from django.utils import timezone
from django.contrib.auth.models import Permission
from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ("Competence", "Competence"),
    ("Awareness/ Trainings", "Awareness/ Trainings"),
    ("Communication", "Communication"),
)

class IMS_07_Folder(models.Model):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    name           = models.CharField(max_length=250)
    category       = models.CharField(max_length=250, choices=CATEGORY_CHOICES)
    description    = models.TextField(blank = True)
    upload_file	   = models.FileField(upload_to='ims_07')
    active         = models.BooleanField(default=True)
    updated        = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp      = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-timestamp", "-updated"]