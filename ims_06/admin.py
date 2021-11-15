from django.contrib import admin
from . models import IMS_06_Folder, BlankForm

# Register your models here.
class IMS_06_FolderModelAdmin(admin.ModelAdmin):
    list_display 		= ["user", "name", "department", "category", "upload_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["department","name", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["department", "description"]
    class Meta:
        model = IMS_06_Folder


# Register your models here.
class BlankFormModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","department", "name", "upload_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["department", "active", "name"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["department", "description"]
    class Meta:
        model = BlankForm

        

admin.site.register(BlankForm, BlankFormModelAdmin)
admin.site.register(IMS_06_Folder, IMS_06_FolderModelAdmin)