from django.contrib import admin
from django.urls import path

from .views import (
    IncidentNonConformityCorrectiveActionListAPIView,
    IncidentNonConformityCorrectiveActionDeleteAPIView,
    IncidentNonConformityCorrectiveActionDetailAPIView,
    IncidentNonConformityCorrectiveActionUpdateAPIView,
    IncidentNonConformityCorrectiveActionCreateAPIView,

	)

urlpatterns = [
    ##### process flow
    path('incident_non_conformity_and_corrective_action/', IncidentNonConformityCorrectiveActionListAPIView.as_view(), name='process_flow'),
    path('incident_non_conformity_and_corrective_action/new/', IncidentNonConformityCorrectiveActionCreateAPIView.as_view(), name='new_chart'),
    path('incident_non_conformity_and_corrective_action/<int:id>/detail/', IncidentNonConformityCorrectiveActionDetailAPIView.as_view(), name='detail_chart'),
    path('incident_non_conformity_and_corrective_action/<int:id>/edit/', IncidentNonConformityCorrectiveActionUpdateAPIView.as_view(), name='update_chart'),
    path('incident_non_conformity_and_corrective_action/<int:id>/delete/', IncidentNonConformityCorrectiveActionDeleteAPIView.as_view(), name="delete_chart"),

]
