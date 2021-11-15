from django.contrib import admin
from django.urls import path

from .views import (
    IMS_07_FolderListAPIView,
    IMS_07_FolderDeleteAPIView,
    IMS_07_FolderDetailAPIView,
    IMS_07_FolderUpdateAPIView,
    IMS_07_FolderCreateAPIView,
	)

urlpatterns = [
    path('ims_07/', IMS_07_FolderListAPIView.as_view(), name='list'),
    path('ims_07/new/', IMS_07_FolderCreateAPIView.as_view(), name='new'),
    path('ims_07/<int:id>/detail/', IMS_07_FolderDetailAPIView.as_view(), name='detail'),
    path('ims_07/<int:id>/edit/', IMS_07_FolderUpdateAPIView.as_view(), name='update'),
    path('ims_07/<int:id>/delete/', IMS_07_FolderDeleteAPIView.as_view(), name="delete"),
]
