from django.contrib import admin

from pages.models import ContactModel, AboutModel

admin.site.register(ContactModel)
admin.site.register(AboutModel)
