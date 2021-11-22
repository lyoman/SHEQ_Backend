from django.contrib import admin
from . models import ActionPlan, ManagementReviewMinute, MonitoringMeasurementAnalysisPerformanceEvaluation

# Register your models here.
class ActionPlanModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "category", "upload_file", "department", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["name", "category", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = ActionPlan

class ManagementReviewMinuteModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "upload_file", "department", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "timestamp", "user"]
    list_editable		= ["name", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = ManagementReviewMinute


class MonitoringMeasurementAnalysisPerformanceEvaluationModelAdmin(admin.ModelAdmin):
    list_display 		= ["user","name", "category", "sub_category", "department", "upload_file", "active", "description", "timestamp", "updated"]
    list_display_links  = ["updated", "category", "timestamp", "user"]
    list_editable		= ["name", "active"]
    list_filter			= ["updated", "timestamp", "description"]
    search_fields		= ["name", "description"]
    class Meta:
        model = MonitoringMeasurementAnalysisPerformanceEvaluation


admin.site.register(MonitoringMeasurementAnalysisPerformanceEvaluation, MonitoringMeasurementAnalysisPerformanceEvaluationModelAdmin)
admin.site.register(ActionPlan, ActionPlanModelAdmin)
admin.site.register(ManagementReviewMinute, ManagementReviewMinuteModelAdmin)