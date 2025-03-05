from django.db import models

# Create your models here.


class Merchandise(models.Model):
    """
    ### MD 모델
    """

    name = models.CharField("상품 이름", max_length=255)
    description = models.TextField("상품 설명", null=True, blank=True)
    image = models.ImageField("썸네일 이미지", upload_to="images/", null=True, blank=True)

    def __str__(self):
        return self.name
