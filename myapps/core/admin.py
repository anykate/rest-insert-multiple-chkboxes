from django.contrib import admin
from .models import Sport


# Register your models here.
class SportAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sport, SportAdmin)
admin.site.site_header = 'Haritha Computers & Technology'
