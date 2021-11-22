from django.contrib import admin
from django.urls import path

from .views import (
    ManagementDocuemntListAPIView,
    ManagementDocuemntDeleteAPIView,
    ManagementDocuemntDetailAPIView,
    ManagementDocuemntUpdateAPIView,
    ManagementDocuemntCreateAPIView,

    OperationalPlanningControlListAPIView,
    OperationalPlanningControlDeleteAPIView,
    OperationalPlanningControlDetailAPIView,
    OperationalPlanningControlUpdateAPIView,
    OperationalPlanningControlCreateAPIView,

	)

urlpatterns = [
    path('management_documents/', ManagementDocuemntListAPIView.as_view(), name='list'),
    path('management_documents/new/', ManagementDocuemntCreateAPIView.as_view(), name='new'),
    path('management_documents/<int:id>/detail/', ManagementDocuemntDetailAPIView.as_view(), name='detail'),
    path('management_documents/<int:id>/edit/', ManagementDocuemntUpdateAPIView.as_view(), name='update'),
    path('management_documents/<int:id>/delete/', ManagementDocuemntDeleteAPIView.as_view(), name="delete"),

    ##### process flow
    path('operational_planning_control/', OperationalPlanningControlListAPIView.as_view(), name='process_flow'),
    path('operational_planning_control/new/', OperationalPlanningControlCreateAPIView.as_view(), name='new_chart'),
    path('operational_planning_control/<int:id>/detail/', OperationalPlanningControlDetailAPIView.as_view(), name='detail_chart'),
    path('operational_planning_control/<int:id>/edit/', OperationalPlanningControlUpdateAPIView.as_view(), name='update_chart'),
    path('operational_planning_control/<int:id>/delete/', OperationalPlanningControlDeleteAPIView.as_view(), name="delete_chart"),

]
