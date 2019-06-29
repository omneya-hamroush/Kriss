from django.contrib import admin

from profiles_api import models


admin.site.register(models.Product)
admin.site.register(models.Gallery)
admin.site.register(models.Picture)
