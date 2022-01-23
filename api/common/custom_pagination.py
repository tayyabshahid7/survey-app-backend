from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(LimitOffsetPagination):
    default_limit = 50
    max_limit = 200
    min_limit = 1
    min_offset = 0
