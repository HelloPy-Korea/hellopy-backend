from drf_spectacular.utils import extend_schema_view
from rest_framework.viewsets import GenericViewSet

from core.responses.base import BaseResponse

from .models import PymonCalendar
from .serializers import PymonCalendarSerializer
from .swagger import PymonCalendarAPIDocs


# Create your views here.
@extend_schema_view(list=PymonCalendarAPIDocs.list())
class PymonCalendarViewSet(GenericViewSet):
    serializer_class = PymonCalendarSerializer

    def get_queryset(self):
        return PymonCalendar.objects.all()

    def list(self, request, *args, **kwargs) -> BaseResponse:
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return BaseResponse(serializer.data)
