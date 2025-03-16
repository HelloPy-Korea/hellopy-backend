from drf_spectacular.utils import OpenApiExample, OpenApiParameter, OpenApiResponse

from core.responses.serializer import (
    ErrorResponseSerializer,
    ListSuccessResponseSerializer,
    SuccessResponseSerializer,
)
from core.swagger import SwaggerSchema


class NoticeAPIDocs(SwaggerSchema):
    sample_notice_detail = {
        "id": 1,
        "title": "공지 사항 제목 1",
        "content": "<div>공지 사항 입니다.</div>",
        "tags": [{"id": 1, "name": "태그1"}, {"id": 2, "name": "태그2"}],
        "is_pinned": True,
        "created_at": "2021-01-01 00:00:00",
        "updated_at": "2021-01-01 00:00:00",
    }
    sample_notice_list = [
        {
            "id": 2,
            "title": "공지 사항 제목 2",
            "tags": [{"id": 1, "name": "태그1"}, {"id": 2, "name": "태그2"}],
            "is_pinned": True,
        },
        {
            "id": 1,
            "title": "공지 사항 제목 1",
            "tags": [{"id": 1, "name": "태그1"}, {"id": 2, "name": "태그2"}],
            "is_pinned": True,
        },
    ]

    @classmethod
    def retrieve(cls):
        responses = {
            "성공": OpenApiResponse(
                response=SuccessResponseSerializer,
                description="단일 응답 성공",
                examples=[
                    OpenApiExample(
                        name="공지 사항 상세 조회",
                        value={
                            "status": "SUCCESS",
                            "data": cls.sample_notice_detail,
                        },
                    ),
                ],
            ),
            "에러": OpenApiResponse(
                response=ErrorResponseSerializer,
                description="응답 에러",
                examples=[
                    OpenApiExample(
                        name="데이터 없음",
                        value={
                            "status": "ERROR",
                            "error": {"code": "NOT_EXIST", "message": "데이터가 없습니다."},
                        },
                    ),
                ],
            ),
        }
        return cls.generate_schema(
            operation_id="notice_retrieve", description="공지 사항 상세 조회", responses=responses
        )

    @classmethod
    def list(cls):
        parameters = [
            OpenApiParameter(
                name="is_pinned",
                type=bool,
                location=OpenApiParameter.QUERY,
                description="고정된 공지만 조회",
            ),
        ]
        responses = {
            "성공": OpenApiResponse(
                response=ListSuccessResponseSerializer,
                description="다중 응답 성공",
                examples=[
                    OpenApiExample(
                        name="공지 사항 목록 조회 (페이지네이션 있음)",
                        value={
                            "status": "SUCCESS",
                            "data": cls.sample_notice_list,
                            "pagination": {
                                "count": 20,
                                "next": "http://localhost:8000/api/v1/notice/?page=2",
                                "previous": "http://localhost:8000/api/v1/notice/?page=1",
                            },
                        },
                    ),
                    OpenApiExample(
                        name="공지 사항 목록 조회 (데이터 있음)",
                        value={
                            "status": "SUCCESS",
                            "data": cls.sample_notice_list,
                            "pagination": {"count": 1, "next": None, "previous": None},
                        },
                    ),
                    OpenApiExample(
                        name="공지 사항 목록 조회 (데이터 없음)",
                        value={
                            "status": "SUCCESS",
                            "data": [],
                            "pagination": {"count": 0, "next": None, "previous": None},
                        },
                    ),
                ],
            ),
            "에러": OpenApiResponse(response=ErrorResponseSerializer, description="응답 에러"),
        }
        return cls.generate_schema(
            operation_id="notice_list",
            description="공지 사항 목록 조회",
            responses=responses,
            parameters=parameters,
        )
