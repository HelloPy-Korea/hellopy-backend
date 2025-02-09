from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework.viewsets import GenericViewSet

from core.errors import NotExistException
from core.responses.base import BaseResponse
from core.responses.serializer import (
    ErrorResponseSerializer,
    ListSuccessResponseSerializer,
    SuccessResponseSerializer,
)

from .models import FAQ
from .serializers import FAQSerializer


class FAQViewSet(GenericViewSet):
    serializer_class = FAQSerializer

    def get_queryset(self):
        """
        ## queryset에서 is_deleted는 제외시켜주는 역할
        """
        return FAQ.objects.filter(is_deleted=False)

    @extend_schema(
        description="모든 FAQ 목록 조회",
        responses={
            "200/성공": ListSuccessResponseSerializer,
            "200/에러": ErrorResponseSerializer,
        },
    )
    def list(self, request, *args, **kwargs):
        """
        ## 모든 FAQ 목록 조회
        ### 특징 : is_deleted는 제외
        """
        queryset = self.get_queryset()
        if not queryset.exists():
            raise NotExistException()
        page = self.paginate_queryset(queryset)  # ✅ 페이지네이션 적용
        serializer = self.get_serializer(page or queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema(
        description="모든 FAQ 목록 조회",
        responses={
            "200/성공": OpenApiResponse(
                response=SuccessResponseSerializer,
                description="응답 성공",
            ),
            "200/에러": OpenApiResponse(
                response=ErrorResponseSerializer,
                description="응답 에러",
            ),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        """
        ## 특정 FAQ 조회
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return BaseResponse(serializer.data)
