from django.db import models

class ProductModel(models.Model):
    img = models.ImageField(upload_to='shop')
    img1 = models.ImageField(upload_to='shop')
    img2 = models.ImageField(upload_to='shop', )
    img3 = models.ImageField(upload_to='shop')
    img4 = models.ImageField(upload_to='shop')
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount = models.FloatField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'