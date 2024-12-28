from django.db import models

class ProductModel(models.Model):
    img = models.ImageField(upload_to='shop')
    name = models.CharField(max_length=50)
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'