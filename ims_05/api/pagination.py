from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class IMS05_FolderLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class IMS05_FolderPageNumberPagination(PageNumberPagination):
    page_size = 10