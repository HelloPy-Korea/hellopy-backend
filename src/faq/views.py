from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import GenericViewSet

from core.errors import NotExistException
from core.responses.base import BaseResponse

from .models import FAQ
from .serializers import FAQSerializer
from .swagger import FAQAPIDocs


@extend_schema_view(list=FAQAPIDocs.list(), retrieve=FAQAPIDocs.retrieve())
class FAQViewSet(GenericViewSet):
    serializer_class = FAQSerializer

    def get_queryset(self):
        return FAQ.objects.filter(is_deleted=False)

    def list(self, request, *args, **kwargs) -> BaseResponse:
        queryset = self.get_queryset()
        if not queryset.exists():
            raise NotExistException()
        page = self.paginate_queryset(queryset)  # ✅ 페이지네이션 적용
        serializer = self.get_serializer(page or queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs) -> BaseResponse:
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return BaseResponse(serializer.data)
