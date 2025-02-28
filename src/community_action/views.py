from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import GenericViewSet

from core.responses.base import BaseResponse

from .models import CommunityAction
from .serializers import CommunityActionSerializer
from .swagger import CommunityActionAPIDocs


@extend_schema_view(list=CommunityActionAPIDocs.list())
class CommunityActionViewSet(GenericViewSet):
    """커뮤니티 활동 API 뷰"""

    serializer_class = CommunityActionSerializer

    def get_queryset(self):
        return CommunityAction.objects.prefetch_related("photos", "community_tags__tag").all()

    def list(self, request, *args, **kwargs) -> BaseResponse:
        """커뮤니티 활동 목록 조회 API"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return BaseResponse(serializer.data)
