from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import GenericViewSet

from core.responses.base import BaseResponse

from .models import Manager
from .serializers import ManagerSerializer
from .swagger import ManagerAPIDocs


@extend_schema_view(list=ManagerAPIDocs.list())
class ManagerViewSet(GenericViewSet):

    serializer_class = ManagerSerializer

    def get_queryset(self):
        return Manager.objects.all()

    def list(self, requset, *args, **kwargs) -> BaseResponse:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return BaseResponse(serializer.data)
