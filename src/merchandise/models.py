import os

from django.db import models


class Merchandise(models.Model):
    """
    ### MD 모델
    """

    name = models.CharField("상품 이름", max_length=255)
    description = models.TextField("상품 설명", null=True, blank=True)
    image = models.ImageField("썸네일 이미지", upload_to="merchandise/image/")

    class Meta:
        verbose_name = "MD 상품 관리"
        verbose_name_plural = "MD 상품 관리"

    def delete(self, *args, **kwargs):
        # 연결된 이미지 파일 삭제
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name
