from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from ims_09.models import ActionPlans, ManagementReviewMinutes, MonitoringMeasurementAnalysisPerformanceEvaluation
# from .serializers import PostSerializer
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


class ActionPlansCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims_09/action_plans')
    class Meta:
        model = ActionPlans
        fields = [
            'id',
            'user',
            'name',
            'category',
            'department',
            'description',
            'upload_file'
        ]


organogram_detail_url = HyperlinkedIdentityField(
        view_name='ims_09-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class ActionPlansDetailSerializer(ModelSerializer):
    url = organogram_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = ActionPlans
        fields = [
            'url',
            'id',
            'user',
            'name',
            'category',
            'department',
            'description',
            'upload_file',
            'active',
            'updated',
            'timestamp'
        ]

class ActionPlansListSerializer(ModelSerializer):
    url = organogram_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_09-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = ActionPlans
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'name',
            'category',
            'department',
            'description',
            'active',
            'upload_file',
            'updated',
            'timestamp'
        ]


#####Process flow Charts
class ManagementReviewMinutesCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims_09/management_review_minutes')
    class Meta:
        model = ManagementReviewMinutes
        fields = [
            'id',
            'user',
            'name',
            'department',
            'description',
            'upload_file'
        ]


chart_detail_url = HyperlinkedIdentityField(
        view_name='ims_09-api:detail_chart',
        lookup_field='id'#or primary key <pk>
    )

class ManagementReviewMinutesDetailSerializer(ModelSerializer):
    url = chart_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = ManagementReviewMinutes
        fields = [
            'url',
            'id',
            'user',
            'name',
            'department',
            'description',
            'upload_file',
            'active',
            'updated',
            'timestamp'
        ]

class ManagementReviewMinutesListSerializer(ModelSerializer):
    url = chart_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_09-api:delete_chart',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = ManagementReviewMinutes
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'name',
            'department',
            'description',
            'upload_file',
            'active',
            'updated',
            'timestamp'
        ]


####### Needs and Expetations
class MonitoringMeasurementAnalysisPerformanceEvaluationCreateUpdateSerializer(ModelSerializer):
    user 		= models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims_09/monitoring_measurement_analysis')
    class Meta:
        model = MonitoringMeasurementAnalysisPerformanceEvaluation
        fields = [
            'id',
            'user',
            'name',
            'category',
            'sub_category',
            'description',
            'upload_file'
        ]


needs_detail_url = HyperlinkedIdentityField(
        view_name='ims_09-api:detail_needs',
        lookup_field='id'#or primary key <pk>
    )

class MonitoringMeasurementAnalysisPerformanceEvaluationDetailSerializer(ModelSerializer):
    url = needs_detail_url
    user = UserDetailSerializer(read_only=True)
    class Meta:
        model = MonitoringMeasurementAnalysisPerformanceEvaluation
        fields = [
            'url',
            'id',
            'user',
            'name',
            'category',
            'sub_category',
            'description',
            'upload_file',
            'active',
            'updated',
            'timestamp'
        ]

class MonitoringMeasurementAnalysisPerformanceEvaluationListSerializer(ModelSerializer):
    url = needs_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_09-api:delete_needs',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = MonitoringMeasurementAnalysisPerformanceEvaluation
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'name',
            'category',
            'sub_category',
            'description',
            'upload_file',
            'active',
            'updated',
            'timestamp'
        ]