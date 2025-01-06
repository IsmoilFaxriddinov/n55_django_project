from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class ContactModel(BaseModel):
    name = models.CharField(max_length=125)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
    
class AboutModel(BaseModel):
    name = models.CharField(max_length=125)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class BlogDetailModel(BaseModel):
    comment = models.TextField()
    name = models.CharField(max_length=125)
    email = models.EmailField()
    website = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Blog detail'
        verbose_name_plural = 'Blog details'
