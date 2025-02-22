from rest_framework.pagination import PageNumberPagination as DRFPageNumberPagination

from .responses.base import BaseResponse


class PageNumberPagination(DRFPageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100  # page 단위의 요청 최대 size

    def get_paginated_response(self, data):
        pagination = {
            "count": self.page.paginator.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
        }
        return BaseResponse(data=data, pagination=pagination)

    def get_paginated_response_schema(self, schema: dict) -> dict:
        return schema
