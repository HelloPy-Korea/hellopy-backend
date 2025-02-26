from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import GenericViewSet

from core.responses.base import BaseResponse

from .models import Notice
from .serializers import NoticeSerializer
from .swagger import NoticeAPIDocs


@extend_schema_view(list=NoticeAPIDocs.list(), retrieve=NoticeAPIDocs.retrieve())
class NoticeViewSet(GenericViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.filter(is_deleted=False)
    filterset_fields = ("is_pinned",)

    def list(self, request, *args, **kwargs) -> BaseResponse:
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page or queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return BaseResponse(data=serializer.data)
