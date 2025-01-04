from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()

    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
    
