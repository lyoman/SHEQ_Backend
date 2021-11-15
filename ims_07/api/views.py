from rest_framework.generics import ListAPIView

from ims_07.models import IMS_07_Folder
# from .serializers import IMS_07_FolderSerializer

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

from .pagination import IMS_07_FolderLimitOffSetPagination , IMS_07_FolderPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    IMS_07_FolderListSerializer,
    IMS_07_FolderDetailSerializer, 
    IMS_07_FolderCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


#Creating an Ambulance
class IMS_07_FolderCreateAPIView(CreateAPIView):
    queryset = IMS_07_Folder.objects.all()
    serializer_class = IMS_07_FolderCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class IMS_07_FolderUpdateAPIView(RetrieveUpdateAPIView):
    queryset = IMS_07_Folder.objects.all()
    serializer_class = IMS_07_FolderCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class IMS_07_FolderDeleteAPIView(DestroyAPIView):
    queryset = IMS_07_Folder.objects.all()
    serializer_class = IMS_07_FolderDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class IMS_07_FolderDetailAPIView(RetrieveAPIView):
    queryset = IMS_07_Folder.objects.all()
    serializer_class = IMS_07_FolderDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class IMS_07_FolderListAPIView(ListAPIView):
    serializer_class = IMS_07_FolderListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'category']
    pagination_class = IMS_07_FolderPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = IMS_07_Folder.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset