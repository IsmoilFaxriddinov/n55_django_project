from django.db import models

class ProfileModel(models.Model):
    avatar = models.ImageField(upload_to='avatars')
    