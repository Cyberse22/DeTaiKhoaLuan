from rest_framework.pagination import PageNumberPagination


class UserPaginator(PageNumberPagination):
    page_size = 4


class ThesisPaginator(PageNumberPagination):
    page_size = 4


class GuardPaginator(PageNumberPagination):
    page_size = 5


class GradePaginator(PageNumberPagination):
    page_size = 4
