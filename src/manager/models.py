from django.db import models


# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=10, verbose_name="이름")
    role = models.CharField(max_length=10, verbose_name="역할")
    email = models.EmailField(unique=True, verbose_name="이메일")
    linkedin = models.TextField(blank=True, null=True, verbose_name="LinkedIn 프로필 URL")
    github = models.TextField(blank=True, null=True, verbose_name="Github 프로필 URL")
    photo = models.ImageField(upload_to="photos/", blank=True, null=True, verbose_name="사진")

    class Meta:
        verbose_name = "운영진"
        verbose_name_plural = "운영진"

    def __str__(self):
        return self.name
