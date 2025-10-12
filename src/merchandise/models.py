from django.db import models

from core.mixins.models import SoftDeleteModel
from public.mixin.img_models import MultiImageFieldMixin


class Merchandise(MultiImageFieldMixin, SoftDeleteModel):
    """
    ### MD 모델
    """

    name = models.CharField("상품 이름", max_length=255)
    description = models.TextField("상품 설명", null=True, blank=True)
    is_visible = models.BooleanField("상품 공개 여부", default=True)
    image = models.ImageField("썸네일 이미지", upload_to="merchandise/image/")

    # MultiImageFieldMixin에서 clean, delete를 위해 필요한 정보 작성
    image_field_names = ["image"]

    class Meta:
        verbose_name = "MD 상품 관리"
        verbose_name_plural = "MD 상품 관리"

    def __str__(self):
        return self.name
