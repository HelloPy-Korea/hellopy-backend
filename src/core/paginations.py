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
        return {
            "type": "object",
            "required": ["pagination", "data", "status"],
            "properties": {
                "status": {"type": "string", "example": "SUCCESS"},
                "pagination": {
                    "type": "object",
                    "properties": {
                        "count": {"type": "integer", "example": 123},
                        "next": {
                            "type": "string",
                            "nullable": True,
                            "format": "uri",
                            "example": "http://api.example.org/accounts/?{page_query_param}=4".format(
                                page_query_param=self.page_query_param
                            ),
                        },
                        "previous": {
                            "type": "string",
                            "nullable": True,
                            "format": "uri",
                            "example": "http://api.example.org/accounts/?{page_query_param}=2".format(
                                page_query_param=self.page_query_param
                            ),
                        },
                    },
                    "example": 123,
                },
                "data": schema,
            },
        }
