from rest_framework.generics import ListAPIView

from ims_08.models import OperationalPlanningControl, ManagementDocument
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
    OperationalPlanningControlListSerializer,
    OperationalPlanningControlDetailSerializer, 
    OperationalPlanningControlCreateUpdateSerializer,

    ManagementDocumentListSerializer,
    ManagementDocumentDetailSerializer, 
    ManagementDocumentCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# class OperationalPlanningControlListAPIView(ListAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeSerializer

#Creating an Ambulance
class OperationalPlanningControlCreateAPIView(CreateAPIView):
    queryset = OperationalPlanningControl.objects.all()
    serializer_class = OperationalPlanningControlCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class OperationalPlanningControlUpdateAPIView(RetrieveUpdateAPIView):
    queryset = OperationalPlanningControl.objects.all()
    serializer_class = OperationalPlanningControlCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class OperationalPlanningControlDeleteAPIView(DestroyAPIView):
    queryset = OperationalPlanningControl.objects.all()
    serializer_class = OperationalPlanningControlDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class OperationalPlanningControlDetailAPIView(RetrieveAPIView):
    queryset = OperationalPlanningControl.objects.all()
    serializer_class = OperationalPlanningControlDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class OperationalPlanningControlListAPIView(ListAPIView):
    serializer_class = OperationalPlanningControlListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = OperationalPlanningControl.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset



#Creating an ManagementDocument
class ManagementDocumentCreateAPIView(CreateAPIView):
    queryset = ManagementDocument.objects.all()
    serializer_class = ManagementDocumentCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class ManagementDocumentUpdateAPIView(RetrieveUpdateAPIView):
    queryset = ManagementDocument.objects.all()
    serializer_class = ManagementDocumentCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class ManagementDocumentDeleteAPIView(DestroyAPIView):
    queryset = ManagementDocument.objects.all()
    serializer_class = ManagementDocumentDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class ManagementDocumentDetailAPIView(RetrieveAPIView):
    queryset = ManagementDocument.objects.all()
    serializer_class = ManagementDocumentDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class ManagementDocumentListAPIView(ListAPIView):
    serializer_class = ManagementDocumentListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = ManagementDocument.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset