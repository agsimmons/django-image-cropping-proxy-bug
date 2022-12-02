from django.db import models

from image_cropping import ImageRatioField


class ExampleModel(models.Model):
    name = models.CharField(max_length=64)

    image = models.ImageField(blank=True)
    image_cropping = ImageRatioField("image", "1x1")

    def __str__(self):
        return self.name


class ExampleProxyModel(ExampleModel):
    class Meta:
        proxy = True
