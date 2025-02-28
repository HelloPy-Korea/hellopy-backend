from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from core.responses.serializer import (
    ErrorResponseSerializer,
    ListSuccessResponseSerializer,
    SuccessResponseSerializer,
)
from core.swagger import SwaggerSchema


class PymonCalendarAPIDocs(SwaggerSchema):
    @classmethod
    def list(cls):
        responses = {
            "성공": OpenApiResponse(
                response=ListSuccessResponseSerializer,
                description="다중 응답 성공",
                examples=[
                    OpenApiExample(
                        name="캘린더 목록 조회",
                        value={
                            "status": "SUCCESS",
                            "data": [
                                {"id": 1, "month": "월", "calendar_photo": "사진 url"},
                            ],
                        },
                    ),
                    OpenApiExample(
                        name="캘린더 목록 조회 (데이터 없음)",
                        value={
                            "status": "SUCCESS",
                            "data": [],
                        },
                    ),
                ],
            ),
            "에러": OpenApiResponse(response=ErrorResponseSerializer, description="응답 에러"),
        }
        return cls.generate_schema(
            operation_id="pymon_calendar_list",
            description="모든 달력 목록 조회",
            responses=responses,
        )
