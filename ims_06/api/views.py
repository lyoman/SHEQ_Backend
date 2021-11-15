from rest_framework.generics import ListAPIView

from ims_06.models import IMS_06_Folder, BlankForm
# from .serializers import IMS_06_FolderSerializer

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

from .pagination import IMS_06_FolderLimitOffSetPagination , IMS_06_FolderPageNumberPagination, BlankFormPageNumberPagination

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    IMS_06_FolderListSerializer,
    IMS_06_FolderDetailSerializer, 
    IMS_06_FolderCreateUpdateSerializer,

    BlankFormListSerializer,
    BlankFormDetailSerializer, 
    BlankFormCreateUpdateSerializer,
    )

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)


#Creating an Ambulance
class IMS_06_FolderCreateAPIView(CreateAPIView):
    queryset = IMS_06_Folder.objects.all()
    serializer_class = IMS_06_FolderCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class IMS_06_FolderUpdateAPIView(RetrieveUpdateAPIView):
    queryset = IMS_06_Folder.objects.all()
    serializer_class = IMS_06_FolderCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class IMS_06_FolderDeleteAPIView(DestroyAPIView):
    queryset = IMS_06_Folder.objects.all()
    serializer_class = IMS_06_FolderDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class IMS_06_FolderDetailAPIView(RetrieveAPIView):
    queryset = IMS_06_Folder.objects.all()
    serializer_class = IMS_06_FolderDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class IMS_06_FolderListAPIView(ListAPIView):
    serializer_class = IMS_06_FolderListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['department', 'category']
    pagination_class = IMS_06_FolderPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = IMS_06_Folder.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset



############## Blank Forms ##############
#Creating an Ambulance
class BlankFormCreateAPIView(CreateAPIView):
    queryset = BlankForm.objects.all()
    serializer_class = BlankFormCreateUpdateSerializer 
    # lookup_field = 'id'
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

class BlankFormUpdateAPIView(RetrieveUpdateAPIView):
    queryset = BlankForm.objects.all()
    serializer_class = BlankFormCreateUpdateSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

class BlankFormDeleteAPIView(DestroyAPIView):
    queryset = BlankForm.objects.all()
    serializer_class = BlankFormDetailSerializer
    lookup_field = 'id'
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # permission_classes = [AllowAny]
    permission_classes = [IsOwnerOrReadOnly]

class BlankFormDetailAPIView(RetrieveAPIView):
    queryset = BlankForm.objects.all()
    serializer_class = BlankFormDetailSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]

class BlankFormListAPIView(ListAPIView):
    serializer_class = BlankFormListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['department', 'name']
    pagination_class = BlankFormPageNumberPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = BlankForm.objects.filter(active=True)
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("hey you", queryset)
        return queryset