from django.contrib import admin
from .models import Location
# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    list_display = ("user", "name_amharic", 'name_afaan_oromo', 'job_type_amharic','job_type_afaan_oromo','width', 'height', 'square')
admin.site.register(Location, LocationAdmin)