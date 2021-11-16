from django.contrib import admin
from . models import OperationalPlanningControl, ManagementDocuemnts

# Register your models here.
class OperationalPlanningControlModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "category", "upload_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["name", "category", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = OperationalPlanningControl


class ManagementDocuemntsModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "category", "upload_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["name", "category", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = ManagementDocuemnts

admin.site.register(OperationalPlanningControl, OperationalPlanningControlModelAdmin)
admin.site.register(ManagementDocuemnts, ManagementDocuemntsModelAdmin)