from django.db import models


class TagModel(models.Model):
    name = models.CharField("태그", max_length=100, unique=True)

    class Meta:
        abstract = True
        
    def __str__(self):
        return self.name