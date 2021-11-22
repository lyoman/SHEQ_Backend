from django.contrib import admin
from django.urls import path

from .views import (
    ActionPlansListAPIView,
    ActionPlansDeleteAPIView,
    ActionPlansDetailAPIView,
    ActionPlansUpdateAPIView,
    ActionPlansCreateAPIView,

    ManagementReviewMinutesListAPIView,
    ManagementReviewMinutesDeleteAPIView,
    ManagementReviewMinutesDetailAPIView,
    ManagementReviewMinutesUpdateAPIView,
    ManagementReviewMinutesCreateAPIView,

    MonitoringMeasurementAnalysisPerformanceEvaluationListAPIView,
    MonitoringMeasurementAnalysisPerformanceEvaluationDeleteAPIView,
    MonitoringMeasurementAnalysisPerformanceEvaluationDetailAPIView,
    MonitoringMeasurementAnalysisPerformanceEvaluationUpdateAPIView,
    MonitoringMeasurementAnalysisPerformanceEvaluationCreateAPIView,
	)

urlpatterns = [
    path('action_plans/', ActionPlansListAPIView.as_view(), name='list'),
    path('action_plans/new/', ActionPlansCreateAPIView.as_view(), name='new'),
    path('action_plans/<int:id>/detail/', ActionPlansDetailAPIView.as_view(), name='detail'),
    path('action_plans/<int:id>/edit/', ActionPlansUpdateAPIView.as_view(), name='update'),
    path('action_plans/<int:id>/delete/', ActionPlansDeleteAPIView.as_view(), name="delete"),

    ##### process flow
    path('management_review_minutes/', ManagementReviewMinutesListAPIView.as_view(), name='process_flow'),
    path('management_review_minutes/new/', ManagementReviewMinutesCreateAPIView.as_view(), name='new_chart'),
    path('management_review_minutes/<int:id>/detail/', ManagementReviewMinutesDetailAPIView.as_view(), name='detail_chart'),
    path('management_review_minutes/<int:id>/edit/', ManagementReviewMinutesUpdateAPIView.as_view(), name='update_chart'),
    path('management_review_minutes/<int:id>/delete/', ManagementReviewMinutesDeleteAPIView.as_view(), name="delete_chart"),

    ##### Needs and Expetations
    path('monitoring_measurement_analysis/', MonitoringMeasurementAnalysisPerformanceEvaluationListAPIView.as_view(), name='needs'),
    path('monitoring_measurement_analysis/new/', MonitoringMeasurementAnalysisPerformanceEvaluationCreateAPIView.as_view(), name='new_needs'),
    path('monitoring_measurement_analysis/<int:id>/detail/', MonitoringMeasurementAnalysisPerformanceEvaluationDetailAPIView.as_view(), name='detail_needs'),
    path('monitoring_measurement_analysis/<int:id>/edit/', MonitoringMeasurementAnalysisPerformanceEvaluationUpdateAPIView.as_view(), name='update_needs'),
    path('monitoring_measurement_analysis/<int:id>/delete/', MonitoringMeasurementAnalysisPerformanceEvaluationDeleteAPIView.as_view(), name="delete_needs"),
]
