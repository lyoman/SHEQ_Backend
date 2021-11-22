from rest_framework.generics import ListAPIView

from ims_09.models import ActionPlans, ManagementReviewMinutes, MonitoringMeasurementAnalysisPerformanceEvaluation
# from .serializers import ActionPlansSerializer

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
    ActionPlansListSerializer,
    ActionPlansDetailSerializer, 
    ActionPlansCreateUpdateSerializer,

    ManagementReviewMinutesListSerializer,
    ManagementReviewMinutesDetailSerializer, 
    ManagementReviewMinutesCreateUpdateSerializer,

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

# class ActionPlansListAPIView(ListAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeSerializer

#Creating an Ambulance
class ActionPlansCreateAPIView(CreateAPIView):
    queryset = ActionPlans.objects.all()
    serializer_class = ActionPlansCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class ActionPlansUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ActionPlans.objects.all()
    serializer_class = ActionPlansCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class ActionPlansDeleteAPIView(DestroyAPIView):
    queryset = ActionPlans.objects.all()
    serializer_class = ActionPlansDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class ActionPlansDetailAPIView(RetrieveAPIView):
    queryset = ActionPlans.objects.all()
    serializer_class = ActionPlansDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ActionPlansListAPIView(ListAPIView):
    serializer_class = ActionPlansListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = ActionPlans.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset



#Creating an ManagementReviewMinutes
class ManagementReviewMinutesCreateAPIView(CreateAPIView):
    queryset = ManagementReviewMinutes.objects.all()
    serializer_class = ManagementReviewMinutesCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class ManagementReviewMinutesUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ManagementReviewMinutes.objects.all()
    serializer_class = ManagementReviewMinutesCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class ManagementReviewMinutesDeleteAPIView(DestroyAPIView):
    queryset = ManagementReviewMinutes.objects.all()
    serializer_class = ManagementReviewMinutesDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class ManagementReviewMinutesDetailAPIView(RetrieveAPIView):
    queryset = ManagementReviewMinutes.objects.all()
    serializer_class = ManagementReviewMinutesDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ManagementReviewMinutesListAPIView(ListAPIView):
    serializer_class = ManagementReviewMinutesListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = ManagementReviewMinutes.objects.filter(active=True)
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