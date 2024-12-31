from django.contrib import admin
from shop import models

@admin.register(models.ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at', 'updated_at']
    ordering = ['-created_at']
