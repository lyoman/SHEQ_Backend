from django.contrib import admin
from . models import IMS05_Folder

# Register your models here.
class IMS05_FolderModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","department", "category", "upload_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["department", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["department", "description"]
    class Meta:
        model = IMS05_Folder

        
admin.site.register(IMS05_Folder, IMS05_FolderModelAdmin)