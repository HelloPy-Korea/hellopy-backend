from django.core.exceptions import PermissionDenied as DjangoPermissionDenied
from django.http import Http404
from rest_framework.exceptions import APIException, NotFound, PermissionDenied
from rest_framework.views import set_rollback

from core.responses.base import BaseResponse


def custom_exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = NotFound(*(exc.args))
    elif isinstance(exc, DjangoPermissionDenied):
        exc = PermissionDenied(*(exc.args))

    if isinstance(exc, APIException):
        headers = {}
        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header
        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait

        error = dict(code=exc.default_code, message=exc.detail)

        set_rollback()
        return BaseResponse(error=error, headers=headers, status="ERROR")

    return None
