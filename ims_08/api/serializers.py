from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from ims_08.models import OperationalPlanningControl, ManagementDocument
# from .serializers import PostSerializer
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


class OperationalPlanningControlCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims08/operational_planning_control')
    class Meta:
        model = OperationalPlanningControl
        fields = [
            'id',
            'user',
            'name',
            'category',
            'description',
            'upload_file'
        ]


organogram_detail_url = HyperlinkedIdentityField(
        view_name='ims_08-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class OperationalPlanningControlDetailSerializer(ModelSerializer):
    url = organogram_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = OperationalPlanningControl
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

class OperationalPlanningControlListSerializer(ModelSerializer):
    url = organogram_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_08-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = OperationalPlanningControl
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


#####Process flow Charts
class ManagementDocumentCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims08/management_documents')
    class Meta:
        model = ManagementDocument
        fields = [
            'id',
            'user',
            'name',
            'category',
            'description',
            'upload_file'
        ]


chart_detail_url = HyperlinkedIdentityField(
        view_name='ims_08-api:detail_chart',
        lookup_field='id'#or primary key <pk>
    )

class ManagementDocumentDetailSerializer(ModelSerializer):
    url = chart_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = ManagementDocument
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

class ManagementDocumentListSerializer(ModelSerializer):
    url = chart_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_08-api:delete_chart',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = ManagementDocument
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'name',
            'category',
            'description',
            'upload_file',
            'active',
            'updated',
            'timestamp'
        ]