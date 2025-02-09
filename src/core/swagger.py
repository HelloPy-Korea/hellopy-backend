import uritemplate
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.plumbing import is_basic_type, is_list_serializer
from drf_spectacular.utils import _SerializerType
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin


class CustomAutoSchema(AutoSchema):
    def _is_list_view(self, serializer: _SerializerType | None = None) -> bool:
        """
        partially heuristic approach to determine if a view yields an object or a
        list of objects. used for operationId naming, array building and pagination.
        defaults to False if all introspection fail.
        """
        if serializer is None:
            serializer = self.get_response_serializers()

        if isinstance(serializer, dict) and serializer:
            # extract likely main serializer from @extend_schema override
            serializer = {str(code): s for code, s in serializer.items()}
            serializer = serializer[min(serializer)]

        if is_list_serializer(serializer):
            return True
        if is_basic_type(serializer):
            return False
        # if hasattr(self.view, 'action'):
        #     return self.view.action == 'list'
        # list responses are "usually" only returned by GET
        if self.method != "GET":
            return False
        if isinstance(self.view, ListModelMixin):
            return True
        # primary key/lookup variable in path is a strong indicator for retrieve
        if isinstance(self.view, GenericAPIView):
            lookup_url_kwarg = self.view.lookup_url_kwarg or self.view.lookup_field
            if lookup_url_kwarg in uritemplate.variables(self.path):
                return False

        return False
