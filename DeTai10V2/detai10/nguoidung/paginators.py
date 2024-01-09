from rest_framework.pagination import PageNumberPagination


class NguoiDungPaginator(PageNumberPagination):
    page_size = 2