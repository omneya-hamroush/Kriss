from django.contrib import admin

from profiles_api import models



class ContactUsAdmin(admin.ModelAdmin):
    model = models.ContactUs
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


class AboutUsAdmin(admin.ModelAdmin):
    model = models.AboutUs
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)





admin.site.register(models.Product)
admin.site.register(models.AboutUs)
admin.site.register(models.Cart)
admin.site.register(models.Picture)
admin.site.register(models.ContactUs)
admin.site.register(models.Store)
admin.site.register(models.Brand)
admin.site.register(models.Category)
admin.site.register(models.LatestOffer)
admin.site.register(models.Family)
admin.site.register(models.CartItem)
admin.site.register(models.Order)
