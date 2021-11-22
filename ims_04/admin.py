from django.contrib import admin
from . models import ComplaintsRegister, NeedsAndExpetation, ProcessFlowChart, Organogram

# Register your models here.
class ComplaintsRegisterModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "complaints_register_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["name", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = ComplaintsRegister

class NeedsAndExpetationModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "needs_expetations_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["name", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = NeedsAndExpetation


class ProcessFlowChartModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "process_chart_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["name", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = ProcessFlowChart


class OrganogramModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "organogram_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["name", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = Organogram
        
admin.site.register(ComplaintsRegister, ComplaintsRegisterModelAdmin)
admin.site.register(NeedsAndExpetation, NeedsAndExpetationModelAdmin)
admin.site.register(ProcessFlowChart, ProcessFlowChartModelAdmin)
admin.site.register(Organogram, OrganogramModelAdmin)