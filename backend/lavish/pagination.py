from rest_framework.pagination import PageNumberPagination

from .settings import REST_FRAMEWORK


class PageNumberAndSizePagination(PageNumberPagination):
    page_size = REST_FRAMEWORK.get('PAGE_SIZE', 25)
    page_size_query_param = 'page_size'
    max_page_size = 1000
