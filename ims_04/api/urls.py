from django.contrib import admin
from django.urls import path

from .views import (
    OrganogramListAPIView,
    OrganogramDeleteAPIView,
    OrganogramDetailAPIView,
    OrganogramUpdateAPIView,
    OrganogramCreateAPIView,

    ProcessFlowChartListAPIView,
    ProcessFlowChartDeleteAPIView,
    ProcessFlowChartDetailAPIView,
    ProcessFlowChartUpdateAPIView,
    ProcessFlowChartCreateAPIView,

    NeedsAndExpetationsListAPIView,
    NeedsAndExpetationsDeleteAPIView,
    NeedsAndExpetationsDetailAPIView,
    NeedsAndExpetationsUpdateAPIView,
    NeedsAndExpetationsCreateAPIView,

    ComplaintsRegisterListAPIView,
    ComplaintsRegisterDeleteAPIView,
    ComplaintsRegisterDetailAPIView,
    ComplaintsRegisterUpdateAPIView,
    ComplaintsRegisterCreateAPIView,
	)

urlpatterns = [
    path('organograms/', OrganogramListAPIView.as_view(), name='Organograms'),
    path('organograms/new/', OrganogramCreateAPIView.as_view(), name='new'),
    path('organograms/<int:id>/detail/', OrganogramDetailAPIView.as_view(), name='detail'),
    path('organograms/<int:id>/edit/', OrganogramUpdateAPIView.as_view(), name='update'),
    path('organograms/<int:id>/delete/', OrganogramDeleteAPIView.as_view(), name="delete"),

    ##### process flow
    path('process_flow/', ProcessFlowChartListAPIView.as_view(), name='process_flow'),
    path('process_flow/new/', ProcessFlowChartCreateAPIView.as_view(), name='new_chart'),
    path('process_flow/<int:id>/detail/', ProcessFlowChartDetailAPIView.as_view(), name='detail_chart'),
    path('process_flow/<int:id>/edit/', ProcessFlowChartUpdateAPIView.as_view(), name='update_chart'),
    path('process_flow/<int:id>/delete/', ProcessFlowChartDeleteAPIView.as_view(), name="delete_chart"),

    ##### Needs and Expetations
    path('needs_expetations/', NeedsAndExpetationsListAPIView.as_view(), name='needs'),
    path('needs_expetations/new/', NeedsAndExpetationsCreateAPIView.as_view(), name='new_needs'),
    path('needs_expetations/<int:id>/detail/', NeedsAndExpetationsDetailAPIView.as_view(), name='detail_needs'),
    path('needs_expetations/<int:id>/edit/', NeedsAndExpetationsUpdateAPIView.as_view(), name='update_needs'),
    path('needs_expetations/<int:id>/delete/', NeedsAndExpetationsDeleteAPIView.as_view(), name="delete_needs"),

    ##### Complaints Register
    path('complaints_register/', ComplaintsRegisterListAPIView.as_view(), name='register'),
    path('complaints_register/new/', ComplaintsRegisterCreateAPIView.as_view(), name='new_register'),
    path('complaints_register/<int:id>/detail/', ComplaintsRegisterDetailAPIView.as_view(), name='detail_register'),
    path('complaints_register/<int:id>/edit/', ComplaintsRegisterUpdateAPIView.as_view(), name='update_register'),
    path('complaints_register/<int:id>/delete/', ComplaintsRegisterDeleteAPIView.as_view(), name="delete_register"),
]
