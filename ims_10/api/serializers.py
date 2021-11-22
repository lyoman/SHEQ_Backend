from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from ims_10.models import IncidentNonConformityCorrectiveAction
# from .serializers import PostSerializer
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


class IncidentNonConformityCorrectiveActionCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims10/all_reports')
    class Meta:
        model = IncidentNonConformityCorrectiveAction
        fields = [
            'id',
            'user',
            'name',
            'category',
            'description',
            'upload_file'
        ]


organogram_detail_url = HyperlinkedIdentityField(
        view_name='ims_10-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class IncidentNonConformityCorrectiveActionDetailSerializer(ModelSerializer):
    url = organogram_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = IncidentNonConformityCorrectiveAction
        fields = [
            'url',
            'id',
            'user',
            'name',
            'category',
            'description',
            'upload_file',
            'active',
            'updated',
            'timestamp'
        ]

class IncidentNonConformityCorrectiveActionListSerializer(ModelSerializer):
    url = organogram_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_10-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = IncidentNonConformityCorrectiveAction
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'name',
            'category',
            'description',
            'active',
            'upload_file',
            'updated',
            'timestamp'
        ]