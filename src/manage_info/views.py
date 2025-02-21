from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import ManagementInfo
from .serializers import ManagementInfoSerializer

class ManagementInfoViewSet(ReadOnlyModelViewSet):
    queryset = ManagementInfo.objects.all()
    serializer_class = ManagementInfoSerializer
