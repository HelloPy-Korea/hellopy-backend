from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import GenericViewSet

from core.responses.base import BaseResponse

from .models import Manager
from .serializers import ManagerSerializer
from .swagger import ManagerAPIDocs


@extend_schema_view(list=ManagerAPIDocs.list())
class ManagerViewSet(GenericViewSet):
    """
    운영진을 세부정보는 없을것이라 판단하고 retrieve는 제외시킴
    """

    serializer_class = ManagerSerializer

    def get_queryset(self):
        return Manager.objects.all()

    def list(self, requset, *args, **kwargs) -> BaseResponse:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return BaseResponse(serializer.data)
