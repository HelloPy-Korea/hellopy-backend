from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from core.responses.serializer import (
    ErrorResponseSerializer,
    ListSuccessResponseSerializer,
)
from core.swagger import SwaggerSchema


class ManagerAPIDocs(SwaggerSchema):
    sample_notice_detail = {
        "id": 1,
        "name": "이름",
        "role": "역할",
        "email": "이메일",
        "linkedin": "링크드인",
        "github": "깃허브",
        "photo": "사진URL",
    }
    sample_notice_list = [
        {
            "id": 2,
            "name": "이름",
            "role": "역할",
            "email": "이메일",
            "linkedin": "링크드인",
            "github": "깃허브",
            "photo": "사진URL",
        },
        {
            "id": 1,
            "name": "이름",
            "role": "역할",
            "email": "이메일",
            "linkedin": "링크드인",
            "github": "깃허브",
            "photo": "사진URL",
        },
    ]

    @classmethod
    def list(cls):
        responses = {
            "성공": OpenApiResponse(
                response=ListSuccessResponseSerializer,
                description="다중 응답 성공",
                examples=[
                    OpenApiExample(
                        name="운영자 목록 조회",
                        value={
                            "status": "SUCCESS",
                            "data": cls.sample_notice_list,
                            "pagination": {},
                        },
                    ),
                    OpenApiExample(
                        name="운영자 목록 조회 (데이터 있음)",
                        value={
                            "status": "SUCCESS",
                            "data": cls.sample_notice_list,
                            "pagination": {},
                        },
                    ),
                    OpenApiExample(
                        name="운영자 목록 조회 (데이터 없음)",
                        value={
                            "status": "SUCCESS",
                            "data": [],
                            "pagination": {},
                        },
                    ),
                ],
            ),
            "에러": OpenApiResponse(response=ErrorResponseSerializer, description="응답 에러"),
        }
        return cls.generate_schema(
            operation_id="manager_list",
            description="운영자 목록 조회",
            responses=responses,
        )
