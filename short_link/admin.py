from django.contrib import admin
from short_link.models import ShortLink


class ShortLinks(admin.ModelAdmin):
    list_display = ('id', 'token', 'link')
    list_display_links = ('id', 'token')
    search_fields = ('link',)
    list_per_page = 20


admin.site.register(ShortLink, ShortLinks)