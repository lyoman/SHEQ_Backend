from rest_framework.generics import ListAPIView

from ims_04.models import Organogram, ProcessFlowChart, NeedsAndExpetations, ComplaintsRegister
# from .serializers import OrganogramSerializer

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
    OrganogramListSerializer,
    OrganogramDetailSerializer, 
    OrganogramCreateUpdateSerializer,

    ProcessFlowChartListSerializer,
    ProcessFlowChartDetailSerializer, 
    ProcessFlowChartCreateUpdateSerializer,

    NeedsAndExpetationsListSerializer,
    NeedsAndExpetationsDetailSerializer, 
    NeedsAndExpetationsCreateUpdateSerializer,

    ComplaintsRegisterListSerializer,
    ComplaintsRegisterDetailSerializer, 
    ComplaintsRegisterCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# class OrganogramListAPIView(ListAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeSerializer

#Creating an Ambulance
class OrganogramCreateAPIView(CreateAPIView):
    queryset = Organogram.objects.all()
    serializer_class = OrganogramCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class OrganogramUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Organogram.objects.all()
    serializer_class = OrganogramCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class OrganogramDeleteAPIView(DestroyAPIView):
    queryset = Organogram.objects.all()
    serializer_class = OrganogramDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class OrganogramDetailAPIView(RetrieveAPIView):
    queryset = Organogram.objects.all()
    serializer_class = OrganogramDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class OrganogramListAPIView(ListAPIView):
    serializer_class = OrganogramListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Organogram.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset



#Creating an ProcessFlowChart
class ProcessFlowChartCreateAPIView(CreateAPIView):
    queryset = ProcessFlowChart.objects.all()
    serializer_class = ProcessFlowChartCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class ProcessFlowChartUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ProcessFlowChart.objects.all()
    serializer_class = ProcessFlowChartCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class ProcessFlowChartDeleteAPIView(DestroyAPIView):
    queryset = ProcessFlowChart.objects.all()
    serializer_class = ProcessFlowChartDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class ProcessFlowChartDetailAPIView(RetrieveAPIView):
    queryset = ProcessFlowChart.objects.all()
    serializer_class = ProcessFlowChartDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ProcessFlowChartListAPIView(ListAPIView):
    serializer_class = ProcessFlowChartListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = ProcessFlowChart.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset


#Creating an NeedsAndExpetations
class NeedsAndExpetationsCreateAPIView(CreateAPIView):
    queryset = NeedsAndExpetations.objects.all()
    serializer_class = NeedsAndExpetationsCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class NeedsAndExpetationsUpdateAPIView(RetrieveUpdateAPIView):
    queryset = NeedsAndExpetations.objects.all()
    serializer_class = NeedsAndExpetationsCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class NeedsAndExpetationsDeleteAPIView(DestroyAPIView):
    queryset = NeedsAndExpetations.objects.all()
    serializer_class = NeedsAndExpetationsDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class NeedsAndExpetationsDetailAPIView(RetrieveAPIView):
    queryset = NeedsAndExpetations.objects.all()
    serializer_class = NeedsAndExpetationsDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class NeedsAndExpetationsListAPIView(ListAPIView):
    serializer_class = NeedsAndExpetationsListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = NeedsAndExpetations.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset



#Creating an ComplaintsRegister
class ComplaintsRegisterCreateAPIView(CreateAPIView):
    queryset = ComplaintsRegister.objects.all()
    serializer_class = ComplaintsRegisterCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class ComplaintsRegisterUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ComplaintsRegister.objects.all()
    serializer_class = ComplaintsRegisterCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class ComplaintsRegisterDeleteAPIView(DestroyAPIView):
    queryset = ComplaintsRegister.objects.all()
    serializer_class = ComplaintsRegisterDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class ComplaintsRegisterDetailAPIView(RetrieveAPIView):
    queryset = ComplaintsRegister.objects.all()
    serializer_class = ComplaintsRegisterDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ComplaintsRegisterListAPIView(ListAPIView):
    serializer_class = ComplaintsRegisterListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = ComplaintsRegister.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset
