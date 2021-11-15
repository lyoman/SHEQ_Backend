from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class IMS_06_FolderLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class IMS_06_FolderPageNumberPagination(PageNumberPagination):
    page_size = 10



class BlankFormLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class BlankFormPageNumberPagination(PageNumberPagination):
    page_size = 10