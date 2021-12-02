from django.contrib import admin
from django.urls import path

from .views import (
    ManagementDocumentListAPIView,
    ManagementDocumentDeleteAPIView,
    ManagementDocumentDetailAPIView,
    ManagementDocumentUpdateAPIView,
    ManagementDocumentCreateAPIView,

    OperationalPlanningControlListAPIView,
    OperationalPlanningControlDeleteAPIView,
    OperationalPlanningControlDetailAPIView,
    OperationalPlanningControlUpdateAPIView,
    OperationalPlanningControlCreateAPIView,

	)

urlpatterns = [
    path('management_documents/', ManagementDocumentListAPIView.as_view(), name='list'),
    path('management_documents/new/', ManagementDocumentCreateAPIView.as_view(), name='new'),
    path('management_documents/<int:id>/detail/', ManagementDocumentDetailAPIView.as_view(), name='detail'),
    path('management_documents/<int:id>/edit/', ManagementDocumentUpdateAPIView.as_view(), name='update'),
    path('management_documents/<int:id>/delete/', ManagementDocumentDeleteAPIView.as_view(), name="delete"),

    ##### process flow
    path('operational_planning_control/', OperationalPlanningControlListAPIView.as_view(), name='process_flow'),
    path('operational_planning_control/new/', OperationalPlanningControlCreateAPIView.as_view(), name='new_chart'),
    path('operational_planning_control/<int:id>/detail/', OperationalPlanningControlDetailAPIView.as_view(), name='detail_chart'),
    path('operational_planning_control/<int:id>/edit/', OperationalPlanningControlUpdateAPIView.as_view(), name='update_chart'),
    path('operational_planning_control/<int:id>/delete/', OperationalPlanningControlDeleteAPIView.as_view(), name="delete_chart"),

]
