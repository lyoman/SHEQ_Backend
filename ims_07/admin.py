from django.contrib import admin
from . models import IMS_07_Folder

# Register your models here.
class IMS_07_FolderModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "category", "upload_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["name", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = IMS_07_Folder

admin.site.register(IMS_07_Folder, IMS_07_FolderModelAdmin)