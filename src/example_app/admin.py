from django.contrib import admin

from image_cropping import ImageCroppingMixin

from example_app import models


@admin.register(models.ExampleModel)
class ExampleModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("name", "image_cropping")
    fields = ("name", "image", "image_cropping")


@admin.register(models.ExampleProxyModel)
class ExampleProxyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("name", "image_cropping")
    fields = ("name", "image", "image_cropping")
