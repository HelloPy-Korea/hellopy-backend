from typing import Any

from django.db import models


class SoftDeleteObjectManager(models.Manager):
    """
    Custom manager to filter out soft-deleted objects by default.
    """

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

    def all_with_deleted(self):
        return super().get_queryset()  # Returns all objects, including soft-deleted ones


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField("숨김 여부", default=False)

    objects = SoftDeleteObjectManager()
    all_objects = models.Manager()  # Manager to access all objects, including soft-deleted

    class Meta:
        abstract = True

    def delete(
        self, using: Any = None, keep_parents: bool = False, force_delete: bool = False
    ) -> None:
        if force_delete:
            return super().delete(using=using, keep_parents=keep_parents)
        self.is_deleted = True
        self.save()
