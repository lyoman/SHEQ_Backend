from rest_framework.generics import ListAPIView

from ims_05.models import IMS05_Folder
# from .serializers import IMS05_FolderSerializer

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

from .pagination import IMS05_FolderLimitOffSetPagination , IMS05_FolderPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    IMS05_FolderListSerializer,
    IMS05_FolderDetailSerializer, 
    IMS05_FolderCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


#Creating an Ambulance
class IMS05_FolderCreateAPIView(CreateAPIView):
    queryset = IMS05_Folder.objects.all()
    serializer_class = IMS05_FolderCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class IMS05_FolderUpdateAPIView(RetrieveUpdateAPIView):
    queryset = IMS05_Folder.objects.all()
    serializer_class = IMS05_FolderCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class IMS05_FolderDeleteAPIView(DestroyAPIView):
    queryset = IMS05_Folder.objects.all()
    serializer_class = IMS05_FolderDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class IMS05_FolderDetailAPIView(RetrieveAPIView):
    queryset = IMS05_Folder.objects.all()
    serializer_class = IMS05_FolderDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class IMS05_FolderListAPIView(ListAPIView):
    serializer_class = IMS05_FolderListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['department', 'category']
    pagination_class = IMS05_FolderPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = IMS05_Folder.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset