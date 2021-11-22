from rest_framework.generics import ListAPIView

from ims_10.models import IncidentNonConformityCorrectiveAction
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
    IncidentNonConformityCorrectiveActionListSerializer,
    IncidentNonConformityCorrectiveActionDetailSerializer, 
    IncidentNonConformityCorrectiveActionCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# class IncidentNonConformityCorrectiveActionListAPIView(ListAPIView):
#     queryset = store.objects.all()
#     serializer_class = storeSerializer

#Creating an Ambulance
class IncidentNonConformityCorrectiveActionCreateAPIView(CreateAPIView):
    queryset = IncidentNonConformityCorrectiveAction.objects.all()
    serializer_class = IncidentNonConformityCorrectiveActionCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class IncidentNonConformityCorrectiveActionUpdateAPIView(RetrieveUpdateAPIView):
    queryset = IncidentNonConformityCorrectiveAction.objects.all()
    serializer_class = IncidentNonConformityCorrectiveActionCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class IncidentNonConformityCorrectiveActionDeleteAPIView(DestroyAPIView):
    queryset = IncidentNonConformityCorrectiveAction.objects.all()
    serializer_class = IncidentNonConformityCorrectiveActionDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class IncidentNonConformityCorrectiveActionDetailAPIView(RetrieveAPIView):
    queryset = IncidentNonConformityCorrectiveAction.objects.all()
    serializer_class = IncidentNonConformityCorrectiveActionDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class IncidentNonConformityCorrectiveActionListAPIView(ListAPIView):
    serializer_class = IncidentNonConformityCorrectiveActionListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    pagination_class = OrganogramPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = IncidentNonConformityCorrectiveAction.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset