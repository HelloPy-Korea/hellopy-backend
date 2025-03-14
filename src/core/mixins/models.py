from typing import Any

from django.db import models


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField("숨김 여부", default=False)

    class Meta:
        abstract = True

    def delete(self, force_delete: bool = False, using: Any = None, keep_parents: bool = False):
        if force_delete:
            return super().delete(using=using, keep_parents=keep_parents)
        self.is_deleted = True
        self.save()
