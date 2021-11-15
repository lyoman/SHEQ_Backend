from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
from ims_06.models import IMS_06_Folder, BlankForm
from rest_framework.serializers import ModelSerializer
from django.db import models
from django.conf import settings


class IMS_06_FolderCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims_06')
    class Meta:
        model = IMS_06_Folder
        fields = [
            'id',
            'user',
            'department',
            'name',
            'category',
            'description',
            'upload_file'
        ]


ims_06_detail_url = HyperlinkedIdentityField(
        view_name='ims_06-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class IMS_06_FolderDetailSerializer(ModelSerializer):
    url = ims_06_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = IMS_06_Folder
        fields = [
            'url',
            'id',
            'user',
            'department',
            'category',
            'name',
            'description',
            'upload_file',
            'active',
            'updated',
            'timestamp'
        ]

class IMS_06_FolderListSerializer(ModelSerializer):
    url = ims_06_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_06-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = IMS_06_Folder
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'department',
            'category',
            'name',
            'description',
            'active',
            'upload_file',
            'updated',
            'timestamp'
        ]


###############Blank forms
class BlankFormCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims_06/blank_forms')
    class Meta:
        model = BlankForm
        fields = [
            'id',
            'user',
            'department',
            'name',
            'category',
            'description',
            'upload_file'
        ]


ims_06_detail_form_url = HyperlinkedIdentityField(
        view_name='ims_06-api:detail_form',
        lookup_field='id'#or primary key <pk>
    )

class BlankFormDetailSerializer(ModelSerializer):
    url = ims_06_detail_form_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = BlankForm
        fields = [
            'url',
            'id',
            'user',
            'department',
            'name',
            'description',
            'upload_file',
            'active',
            'updated',
            'timestamp'
        ]

class BlankFormListSerializer(ModelSerializer):
    url = ims_06_detail_form_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_06-api:delete_form',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = BlankForm
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'department',
            'name',
            'description',
            'active',
            'upload_file',
            'updated',
            'timestamp'
        ]