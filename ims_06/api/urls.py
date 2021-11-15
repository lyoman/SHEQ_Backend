from django.contrib import admin
from django.urls import path

from .views import (
    IMS_06_FolderListAPIView,
    IMS_06_FolderDeleteAPIView,
    IMS_06_FolderDetailAPIView,
    IMS_06_FolderUpdateAPIView,
    IMS_06_FolderCreateAPIView,

    BlankFormListAPIView,
    BlankFormDeleteAPIView,
    BlankFormDetailAPIView,
    BlankFormUpdateAPIView,
    BlankFormCreateAPIView,
	)

urlpatterns = [
    path('ims_06/', IMS_06_FolderListAPIView.as_view(), name='list'),
    path('ims_06/new/', IMS_06_FolderCreateAPIView.as_view(), name='new'),
    path('ims_06/<int:id>/detail/', IMS_06_FolderDetailAPIView.as_view(), name='detail'),
    path('ims_06/<int:id>/edit/', IMS_06_FolderUpdateAPIView.as_view(), name='update'),
    path('ims_06/<int:id>/delete/', IMS_06_FolderDeleteAPIView.as_view(), name="delete"),

    ############ blank forms
    path('ims_06/blank_forms/', BlankFormListAPIView.as_view(), name='list_form'),
    path('ims_06/blank_forms/new/', BlankFormCreateAPIView.as_view(), name='new_form'),
    path('ims_06/blank_forms/<int:id>/detail/', BlankFormDetailAPIView.as_view(), name='detail_form'),
    path('ims_06/blank_forms/<int:id>/edit/', BlankFormUpdateAPIView.as_view(), name='update_form'),
    path('ims_06/blank_forms/<int:id>/delete/', BlankFormDeleteAPIView.as_view(), name="delete_form"),
]
