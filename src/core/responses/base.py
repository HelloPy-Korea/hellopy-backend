from typing import Literal

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class BaseResponse(Response):
    def __init__(
        self,
        data: dict | list | None = None,
        error: dict | None = None,
        pagination: dict | None = None,
        template_name: str | None = None,
        headers: dict | None = None,
        exception: bool = False,
        content_type: str | None = None,
        status: Literal["SUCCESS", "ERROR"] = "SUCCESS",
    ):
        response_format = {
            "status": status,
            "error": error,
            "data": data,
            "pagination": pagination,
        }
        super().__init__(
            response_format, HTTP_200_OK, template_name, headers, exception, content_type
        )

    def __class_getitem__(cls, *args, **kwargs):
        return cls
