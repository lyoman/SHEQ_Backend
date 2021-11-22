from rest_framework.generics import ListAPIView

from ims_09.models import ActionPlan, ManagementReviewMinute, MonitoringMeasurementAnalysisPerformanceEvaluation
# from .serializers import ActionPlanSerializer

from django.db.models import Q

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

from rest_framework.generics import (
    DestroyAPIView,
    ListAPIView, 
    CreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,)

from .pagination import OrganogramLimitOffSetPagination , OrganogramPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    ActionPlanListSerializer,
    ActionPlanDetailSerializer, 
    ActionPlanCreateUpdateSerializer,

    ManagementReviewMinuteListSerializer,
    ManagementReviewMinuteDetailSerializer, 
    ManagementReviewMinuteCreateUpdateSerializer,

    MonitoringMeasurementAnalysisPerformanceEvaluationListSerializer,
    MonitoringMeasurementAnalysisPerformanceEvaluationDetailSerializer, 
    MonitoringMeasurementAnalysisPerformanceEvaluationCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# class ActionPlanListAPIView(ListAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeSerializer

#Creating an Ambulance
class ActionPlanCreateAPIView(CreateAPIView):
    queryset = ActionPlan.objects.all()
    serializer_class = ActionPlanCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class ActionPlanUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ActionPlan.objects.all()
    serializer_class = ActionPlanCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class ActionPlanDeleteAPIView(DestroyAPIView):
    queryset = ActionPlan.objects.all()
    serializer_class = ActionPlanDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class ActionPlanDetailAPIView(RetrieveAPIView):
    queryset = ActionPlan.objects.all()
    serializer_class = ActionPlanDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ActionPlanListAPIView(ListAPIView):
    serializer_class = ActionPlanListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = ActionPlan.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset



#Creating an ManagementReviewMinute
class ManagementReviewMinuteCreateAPIView(CreateAPIView):
    queryset = ManagementReviewMinute.objects.all()
    serializer_class = ManagementReviewMinuteCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class ManagementReviewMinuteUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ManagementReviewMinute.objects.all()
    serializer_class = ManagementReviewMinuteCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class ManagementReviewMinuteDeleteAPIView(DestroyAPIView):
    queryset = ManagementReviewMinute.objects.all()
    serializer_class = ManagementReviewMinuteDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class ManagementReviewMinuteDetailAPIView(RetrieveAPIView):
    queryset = ManagementReviewMinute.objects.all()
    serializer_class = ManagementReviewMinuteDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ManagementReviewMinuteListAPIView(ListAPIView):
    serializer_class = ManagementReviewMinuteListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = ManagementReviewMinute.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset


#Creating an MonitoringMeasurementAnalysisPerformanceEvaluation
class MonitoringMeasurementAnalysisPerformanceEvaluationCreateAPIView(CreateAPIView):
    queryset = MonitoringMeasurementAnalysisPerformanceEvaluation.objects.all()
    serializer_class = MonitoringMeasurementAnalysisPerformanceEvaluationCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class MonitoringMeasurementAnalysisPerformanceEvaluationUpdateAPIView(RetrieveUpdateAPIView):
    queryset = MonitoringMeasurementAnalysisPerformanceEvaluation.objects.all()
    serializer_class = MonitoringMeasurementAnalysisPerformanceEvaluationCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class MonitoringMeasurementAnalysisPerformanceEvaluationDeleteAPIView(DestroyAPIView):
    queryset = MonitoringMeasurementAnalysisPerformanceEvaluation.objects.all()
    serializer_class = MonitoringMeasurementAnalysisPerformanceEvaluationDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class MonitoringMeasurementAnalysisPerformanceEvaluationDetailAPIView(RetrieveAPIView):
    queryset = MonitoringMeasurementAnalysisPerformanceEvaluation.objects.all()
    serializer_class = MonitoringMeasurementAnalysisPerformanceEvaluationDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class MonitoringMeasurementAnalysisPerformanceEvaluationListAPIView(ListAPIView):
    serializer_class = MonitoringMeasurementAnalysisPerformanceEvaluationListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = MonitoringMeasurementAnalysisPerformanceEvaluation.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset