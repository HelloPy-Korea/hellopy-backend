from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Md
from .serializers import MdSerializer

class MdViewSet(ReadOnlyModelViewSet):
    queryset = Md.objects.prefetch_related("md_tags__tag")
    serializer_class = MdSerializer
