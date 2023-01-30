from django.contrib import admin

from . import models

@admin.register(models.Product)
class ProductsAdmin(admin.ModelAdmin):
    pass