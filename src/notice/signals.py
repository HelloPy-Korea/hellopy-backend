from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from django_ckeditor_5.signals import extract_image_paths

from core.storage import s3_delete_file
from notice.models import Notice
from public.image_models import TemporaryImage


@receiver(post_save, sender=Notice)
def delete_temporary_images_on_notice_save(sender, instance, **kwargs):
    images_to_delete = extract_image_paths(instance.content)

    try:
        for img_path in images_to_delete:
            file_path = img_path.removeprefix(f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/")
            delete_images = TemporaryImage.objects.filter(path=file_path).all()
            for image in delete_images:
                image.soft_delete()
    except Exception as e:
        raise ValidationError(f"이미지 삭제 오류: {e}")


@receiver(pre_save, sender=Notice)
def cleanup_unused_ckeditor_images_on_update(sender, instance, **kwargs):
    """
    Removes unused images when an object is updated.
    If any unexpected error occurs, it will be logged, but the deletion process won't break the update.
    """
    try:
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            old_images = set(extract_image_paths(old_instance.content))
        except sender.DoesNotExist:
            old_images = set()

        new_images = set(extract_image_paths(instance.content))
        unused_images = old_images - new_images

        for image in unused_images:
            # CKEditor5Field의 이미지 경로는 상대 경로이므로, 절대 경로로 변환
            file_path = image.removeprefix(f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/")
            s3_delete_file(file_path)
    except Exception as e:
        print(f"Error in cleanup_unused_ckeditor_images_on_update: {e}")


@receiver(pre_delete, sender=Notice)
def cleanup_ckeditor_images_on_delete(sender, instance, **kwargs):
    """
    Removes images from disk when an object is deleted.
    If an error occurs, it is logged, but the deletion process continues.
    """
    try:
        for image in extract_image_paths(instance.content):
            file_path = image.removeprefix(f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/")
            s3_delete_file(file_path)
    except Exception as e:
        print(f"Error in cleanup_ckeditor_images_on_delete: {e}")
