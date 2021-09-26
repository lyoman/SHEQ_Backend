from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from ims_04.models import Organogram, ProcessFlowChart, NeedsAndExpetations, ComplaintsRegister
# from .serializers import PostSerializer
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


class OrganogramCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    organogram_file = models.FileField(upload_to='organograms')
    class Meta:
        model = Organogram
        fields = [
            'id',
            'user',
            'name',
            'description',
            'organogram_file'
        ]


organogram_detail_url = HyperlinkedIdentityField(
        view_name='ims_04-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class OrganogramDetailSerializer(ModelSerializer):
    url = organogram_detail_url
    user = UserDetailSerializer(read_only=True)
    approvedby = UserDetailSerializer(read_only=True)
    # store_logo = SerializerMethodField()
    class Meta:
        model = Organogram
        fields = [
            'url',
            'id',
            'user',
            'name',
            'description',
            'organogram_file',
            'updated',
            'timestamp'
        ]

class OrganogramListSerializer(ModelSerializer):
    url = organogram_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_04-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = Organogram
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'name',
            'description',
            'organogram_file',
            'updated',
            'timestamp'
        ]


#####Process flow Charts
class ProcessFlowChartCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    process_chart_file = models.FileField(upload_to='process_flow_chart')
    class Meta:
        model = ProcessFlowChart
        fields = [
            'id',
            'user',
            'name',
            'description',
            'process_chart_file'
        ]


chart_detail_url = HyperlinkedIdentityField(
        view_name='ims_04-api:detail_chart',
        lookup_field='id'#or primary key <pk>
    )

class ProcessFlowChartDetailSerializer(ModelSerializer):
    url = chart_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = ProcessFlowChart
        fields = [
            'url',
            'id',
            'user',
            'name',
            'description',
            'process_chart_file',
            'updated',
            'timestamp'
        ]

class ProcessFlowChartListSerializer(ModelSerializer):
    url = chart_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_04-api:delete_chart',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = ProcessFlowChart
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'name',
            'description',
            'process_chart_file',
            'updated',
            'timestamp'
        ]


####### Needs and Expetations
class NeedsAndExpetationsCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    needs_expetations_file = models.FileField(upload_to='needs_expetations')
    class Meta:
        model = NeedsAndExpetations
        fields = [
            'id',
            'user',
            'name',
            'description',
            'needs_expetations_file'
        ]


needs_detail_url = HyperlinkedIdentityField(
        view_name='ims_04-api:detail_needs',
        lookup_field='id'#or primary key <pk>
    )

class NeedsAndExpetationsDetailSerializer(ModelSerializer):
    url = needs_detail_url
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = NeedsAndExpetations
        fields = [
            'url',
            'id',
            'user',
            'name',
            'description',
            'needs_expetations_file',
            'updated',
            'timestamp'
        ]

class NeedsAndExpetationsListSerializer(ModelSerializer):
    url = needs_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_04-api:delete_needs',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = NeedsAndExpetations
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'name',
            'description',
            'needs_expetations_file',
            'updated',
            'timestamp'
        ]

######## Complaints Register
class ComplaintsRegisterCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    complaints_register_file = models.FileField(upload_to='complaints_register')
    class Meta:
        model = ComplaintsRegister
        fields = [
            'id',
            'user',
            'name',
            'description',
            'complaints_register_file'
        ]


register_detail_url = HyperlinkedIdentityField(
        view_name='ims_04-api:detail_register',
        lookup_field='id'#or primary key <pk>
    )

class ComplaintsRegisterDetailSerializer(ModelSerializer):
    url = register_detail_url
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = ComplaintsRegister
        fields = [
            'url',
            'id',
            'user',
            'name',
            'description',
            'complaints_register_file',
            'updated',
            'timestamp'
        ]

class ComplaintsRegisterListSerializer(ModelSerializer):
    url = register_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_04-api:delete_register',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = ComplaintsRegister
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'name',
            'description',
            'complaints_register_file',
            'updated',
            'timestamp'
        ]