from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
from ims_07.models import IMS_07_Folder
from rest_framework.serializers import ModelSerializer
from django.db import models
from django.conf import settings


class IMS_07_FolderCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims_07')
    class Meta:
        model = IMS_07_Folder
        fields = [
            'id',
            'user',
            'name',
            'category',
            'description',
            'upload_file'
        ]


ims_07_detail_url = HyperlinkedIdentityField(
        view_name='ims_07-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class IMS_07_FolderDetailSerializer(ModelSerializer):
    url = ims_07_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = IMS_07_Folder
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

class IMS_07_FolderListSerializer(ModelSerializer):
    url = ims_07_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_07-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = IMS_07_Folder
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