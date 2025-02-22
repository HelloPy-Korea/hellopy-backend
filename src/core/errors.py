from rest_framework import status
from rest_framework.exceptions import APIException


class BaseException(APIException):
    status_code = status.HTTP_200_OK
    default_detail = "Internal Server Error"
    default_code = "ERROR"


class NotExistException(BaseException):
    status_code = status.HTTP_200_OK
    default_detail = "Not Exist."
    default_code = "Not Exist"
