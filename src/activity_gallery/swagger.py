from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from core.responses.serializer import (
    ErrorResponseSerializer,
    ListSuccessResponseSerializer,
    SuccessResponseSerializer,
)
from core.swagger import SwaggerSchema


class ActivityActionAPIDocs(SwaggerSchema):
    """커뮤니티 활동 API 문서"""

    @classmethod
    def list(cls):
        """커뮤니티 활동 목록 조회 문서"""
        responses = {
            "성공": OpenApiResponse(
                response=ListSuccessResponseSerializer,
                description="커뮤니티 활동 목록 조회 성공",
                examples=[
                    OpenApiExample(
                        name="커뮤니티 활동 목록 조회",
                        value={
                            "status": "SUCCESS",
                            "data": [
                                {
                                    "id": 1,
                                    "title": "활동",
                                    "tags": [
                                        {"id": 1, "name": "python"},
                                        {"id": 2, "name": "문법"},
                                    ],
                                },
                                {
                                    "id": 2,
                                    "title": "파이콘",
                                    "tags": [],
                                },
                            ],
                        },
                    ),
                    OpenApiExample(
                        name="커뮤니티 활동 목록 조회 (데이터 없음)",
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
            operation_id="activity_action_list",
            description="모든 커뮤니티 활동 목록 조회",
            responses=responses,
        )

    @classmethod
    def retrieve(cls):
        """커뮤니티 활동 상세 조회 문서"""
        responses = {
            "성공": OpenApiResponse(
                response=SuccessResponseSerializer,
                description="커뮤니티 활동 상세 조회 성공",
                examples=[
                    OpenApiExample(
                        name="커뮤니티 활동 상세 조회",
                        value={
                            "status": "SUCCESS",
                            "data": {
                                "id": 1,
                                "title": "활동",
                                "content": "월드 와이드 파이콘",
                                "tags": [
                                    {"id": 1, "name": "python"},
                                    {"id": 2, "name": "문법"},
                                ],
                                "photos": [
                                    {"id": 1, "image": "/media/activity_photos/photo1.jpg"},
                                    {"id": 2, "image": "/media/activity_photos/photo2.jpg"},
                                ],
                            },
                        },
                    ),
                ],
            ),
            "에러": OpenApiResponse(response=ErrorResponseSerializer, description="응답 에러"),
        }
        return cls.generate_schema(
            operation_id="activity_action_retrieve",
            description="특정 커뮤니티 활동 상세 조회",
            responses=responses,
        )
