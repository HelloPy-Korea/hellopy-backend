from django.db import models

from public.mixin.img_models import ImageFieldMixin


class Merchandise(ImageFieldMixin, models.Model):
    """
    ### MD 모델
    """

    name = models.CharField("상품 이름", max_length=255)
    description = models.TextField("상품 설명", null=True, blank=True)
    image = models.ImageField("썸네일 이미지", upload_to="merchandise/image/")

    class Meta:
        verbose_name = "MD 상품 관리"
        verbose_name_plural = "MD 상품 관리"

    def __str__(self):
        return self.name
