from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from ims_09.models import ActionPlan, ManagementReviewMinute, MonitoringMeasurementAnalysisPerformanceEvaluation
# from .serializers import PostSerializer
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


class ActionPlanCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims_09/action_plans')
    class Meta:
        model = ActionPlan
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

class ActionPlanDetailSerializer(ModelSerializer):
    url = organogram_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = ActionPlan
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

class ActionPlanListSerializer(ModelSerializer):
    url = organogram_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_09-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = ActionPlan
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
class ManagementReviewMinuteCreateUpdateSerializer(ModelSerializer):
    user 		    = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    upload_file = models.FileField(upload_to='ims_09/management_review_minutes')
    class Meta:
        model = ManagementReviewMinute
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

class ManagementReviewMinuteDetailSerializer(ModelSerializer):
    url = chart_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = ManagementReviewMinute
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

class ManagementReviewMinuteListSerializer(ModelSerializer):
    url = chart_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='ims_09-api:delete_chart',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = ManagementReviewMinute
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