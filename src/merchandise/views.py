from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import GenericViewSet

from core.responses.base import BaseResponse

from .models import Merchandise
from .serializers import MerchandiseSerializer
from .swagger import MerchandiseAPIDocs


@extend_schema_view(list=MerchandiseAPIDocs.list())
class MerchandiseViewSet(GenericViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer

    def list(self, request, *args, **kwargs) -> BaseResponse:
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page or queryset, many=True)
        return self.get_paginated_response(serializer.data)
