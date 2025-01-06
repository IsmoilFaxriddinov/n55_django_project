from django.contrib import admin

from pages.models import ContactModel, AboutModel, BlogDetailModel

admin.site.register(ContactModel)
admin.site.register(AboutModel)
admin.site.register(BlogDetailModel)
