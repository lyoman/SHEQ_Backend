from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
from ims_05.models import IMS05_Folder
from rest_framework.serializers import ModelSerializer
from django.db import models
from django.conf import settings


class IMS05_FolderCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims_05')
    class Meta:
        model = IMS05_Folder
        fields = [
            'id',
            'user',
            'department',
            'category',
            'description',
            'upload_file'
        ]


ims_05_detail_url = HyperlinkedIdentityField(
        view_name='ims_05-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class IMS05_FolderDetailSerializer(ModelSerializer):
    url = ims_05_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = IMS05_Folder
        fields = [
            'url',
            'id',
            'user',
            'department',
            'category',
            'description',
            'upload_file',
            'active',
            'updated',
            'timestamp'
        ]

class IMS05_FolderListSerializer(ModelSerializer):
    url = ims_05_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_05-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = IMS05_Folder
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'department',
            'category',
            'description',
            'active',
            'upload_file',
            'updated',
            'timestamp'
        ]