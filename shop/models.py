from django.db import models

from pages.models import BaseModel

class ProductModel(BaseModel):
    img = models.ImageField(upload_to='shop')
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    