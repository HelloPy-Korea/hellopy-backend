from drf_spectacular.utils import extend_schema_view
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from core.responses.base import BaseResponse

from .models import ActivityAction
from .serializers import (
    ActivityActionDetailSerializer,
    ActivityActionListSerializer,
)
from .swagger import ActivityActionAPIDocs


@extend_schema_view(
    list=ActivityActionAPIDocs.list(),
    retrieve=ActivityActionAPIDocs.retrieve(),
)
class ActivityActionViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """커뮤니티 활동 API 뷰"""

    def get_queryset(self):
        """공통 쿼리셋"""
        return ActivityAction.objects.prefetch_related("photos", "activity_tags__tag").all()

    def get_serializer_class(self):
        """요청 방식에 따라 적절한 Serializer 반환"""
        if self.action == "list":
            return ActivityActionListSerializer  # 목록 조회에서는 최소한의 데이터만 반환
        elif self.action == "retrieve":
            return ActivityActionDetailSerializer  # 상세 조회에서는 전체 데이터를 반환
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs) -> BaseResponse:
        """커뮤니티 활동 목록 조회 API"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return BaseResponse(serializer.data)

    def retrieve(self, request, *args, **kwargs) -> BaseResponse:
        """커뮤니티 활동 상세 조회 API"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return BaseResponse(serializer.data)
