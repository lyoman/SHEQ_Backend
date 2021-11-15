from django.contrib import admin
from django.urls import path

from .views import (
    IMS05_FolderListAPIView,
    IMS05_FolderDeleteAPIView,
    IMS05_FolderDetailAPIView,
    IMS05_FolderUpdateAPIView,
    IMS05_FolderCreateAPIView,
	)

urlpatterns = [
    path('ims_05/', IMS05_FolderListAPIView.as_view(), name='list'),
    path('ims_05/new/', IMS05_FolderCreateAPIView.as_view(), name='new'),
    path('ims_05/<int:id>/detail/', IMS05_FolderDetailAPIView.as_view(), name='detail'),
    path('ims_05/<int:id>/edit/', IMS05_FolderUpdateAPIView.as_view(), name='update'),
    path('ims_05/<int:id>/delete/', IMS05_FolderDeleteAPIView.as_view(), name="delete"),
]
