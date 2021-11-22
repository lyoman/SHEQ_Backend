from django.contrib import admin
from . models import IncidentNonConformityCorrectiveAction

# Register your models here.
class IncidentNonConformityCorrectiveActionModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "category", "upload_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["name", "category", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = IncidentNonConformityCorrectiveAction


admin.site.register(IncidentNonConformityCorrectiveAction, IncidentNonConformityCorrectiveActionModelAdmin)