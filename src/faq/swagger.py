from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from core.responses.serializer import (
    ErrorResponseSerializer,
    ListSuccessResponseSerializer,
    SuccessResponseSerializer,
)
from core.swagger import SwaggerSchema


class FAQAPIDocs(SwaggerSchema):
    @classmethod
    def retrieve(cls):
        responses = {
            "성공": OpenApiResponse(
                response=SuccessResponseSerializer,
                description="단일 응답 성공",
                examples=[
                    OpenApiExample(
                        name="FAQ 조회",
                        value={
                            "status": "SUCCESS",
                            "data": {
                                "id": 1,
                                "question": "질문",
                                "answer": "답변",
                                "created_at": "2021-01-01",
                            },
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
            operation_id="faq_retrieve", description="FAQ 조회", responses=responses
        )

    @classmethod
    def list(cls):
        responses = {
            "성공": OpenApiResponse(
                response=ListSuccessResponseSerializer,
                description="다중 응답 성공",
                examples=[
                    OpenApiExample(
                        name="FAQ 목록 조회 (페이지네이션 있음)",
                        value={
                            "status": "SUCCESS",
                            "data": [
                                {
                                    "id": 1,
                                    "question": "질문1",
                                    "answer": "답변1",
                                },
                            ],
                            "pagination": {
                                "count": 20,
                                "next": "http://localhost:8000/api/v1/faqs/?page=2",
                                "previous": "http://localhost:8000/api/v1/faqs/?page=1",
                            },
                        },
                    ),
                    OpenApiExample(
                        name="FAQ 목록 조회 (데이터 있음)",
                        value={
                            "status": "SUCCESS",
                            "data": [
                                {
                                    "id": 1,
                                    "question": "질문1",
                                    "answer": "답변1",
                                },
                            ],
                            "pagination": {"count": 1, "next": None, "previous": None},
                        },
                    ),
                    OpenApiExample(
                        name="FAQ 목록 조회 (데이터 없음)",
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
            operation_id="faq_list", description="모든 FAQ 목록 조회", responses=responses
        )
