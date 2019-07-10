from rest_framework import pagination


class NotPaginatedSetPagination(pagination.PageNumberPagination):
    page_size = None
