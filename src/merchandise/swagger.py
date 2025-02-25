from drf_spectacular.utils import OpenApiExample, OpenApiResponse

from core.responses.serializer import (
    ErrorResponseSerializer,
    ListSuccessResponseSerializer,
)
from core.swagger import SwaggerSchema


class MerchandiseAPIDocs(SwaggerSchema):
    @classmethod
    def list(cls):
        responses = {
            "성공": OpenApiResponse(
                response=ListSuccessResponseSerializer,
                description="다중 응답 성공",
                examples=[
                    OpenApiExample(
                        name="상품 목록 조회 (페이지네이션 있음)",
                        value={
                            "status": "SUCCESS",
                            "data": [
                                {
                                    "id": 1,
                                    "product_name": "상품1",
                                    "product_info": "상품 설명입니다.",
                                    "image": "http://localhost:8000/media/merchandise/1.jpg",
                                },
                            ],
                            "pagination": {
                                "count": 20,
                                "next": "http://localhost:8000/api/v1/merchandise/?page=2",
                                "previous": "http://localhost:8000/api/v1/merchandise/?page=1",
                            },
                        },
                    ),
                    OpenApiExample(
                        name="상품 목록 조회 (데이터 있음)",
                        value={
                            "status": "SUCCESS",
                            "data": [
                                {
                                    "id": 1,
                                    "product_name": "상품1",
                                    "product_info": "상품 설명입니다.",
                                    "image": "http://localhost:8000/media/merchandise/1.jpg",
                                },
                            ],
                            "pagination": {"count": 1, "next": None, "previous": None},
                        },
                    ),
                    OpenApiExample(
                        name="Merchandise 목록 조회 (데이터 없음)",
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
            operation_id="merchandise_list", description="모든 상품 목록 조회", responses=responses
        )
