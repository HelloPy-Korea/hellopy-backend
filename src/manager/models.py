from django.db import models

from public.mixin.img_models import MultiImageFieldMixin


# Create your models here.
class Manager(MultiImageFieldMixin):
    name = models.CharField(max_length=10, verbose_name="이름")
    role = models.CharField(max_length=10, verbose_name="역할")
    email = models.EmailField(unique=True, verbose_name="이메일")
    linkedin = models.TextField(blank=True, null=True, verbose_name="LinkedIn 프로필 URL")
    github = models.TextField(blank=True, null=True, verbose_name="Github 프로필 URL")
    photo = models.ImageField(
        upload_to="manager/photo/", blank=True, null=True, verbose_name="사진"
    )

    # MultiImageFieldMixin에서 clean, delete를 위해 필요한 정보 작성
    image_field_names = ["photo"]

    class Meta:
        verbose_name = "운영진 관리"
        verbose_name_plural = "운영진 관리"

    def __str__(self):
        return self.name
