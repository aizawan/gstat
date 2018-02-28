from django.contrib import admin
from cms.models import Resource


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'is_available', 'locking_user')
    list_display_links = ('hostname', 'is_available', 'locking_user')


admin.site.register(Resource, ResourceAdmin)
