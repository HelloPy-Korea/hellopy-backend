import boto3
from django.conf import settings


def s3_delete_file(file_name: str) -> None:
    storage = boto3.client(
        "s3",
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    storage.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key=file_name)
