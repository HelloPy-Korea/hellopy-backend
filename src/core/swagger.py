from typing import Callable

from drf_spectacular.utils import extend_schema


class SwaggerSchema:
    @classmethod
    def generate_schema(cls, *args, **kwargs) -> Callable:
        return extend_schema(*args, **kwargs)
