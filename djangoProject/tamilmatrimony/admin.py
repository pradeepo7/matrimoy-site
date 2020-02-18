from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import profiles
# Register your models here.


class ProfileModelAdmin(ImageCroppingMixin,admin.ModelAdmin):
    list_display = ["tmId","__str__","image", 'timestamp', 'updated']
    list_display_links = ["__str__"]
    list_filter = ["gender","timestamp","dateOfBirth"]
    search_fields = ["name","countryOfOrigin","motherTongue"]


    class Meta:
        model = profiles

admin.site.register(profiles, ProfileModelAdmin)

