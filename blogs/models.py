from django.db import models
from django.contrib.auth.models import User
from pages.models import BaseModel


class BlogCategoryModel(BaseModel):
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'blog category'
        verbose_name_plural = 'blog categories'

class BlogHashganModel(BaseModel):
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'blog hashtag'
        verbose_name_plural = 'blog hashtags'

class BlogModel(BaseModel):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='blogs', null=True, blank=True)
    image = models.ImageField(upload_to='blogs')
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    hashtags = models.ManyToManyField(BlogHashganModel, related_name='blogs')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
