from django.contrib import admin

from adverts.models import Adverts, Status, Category


class AdvertsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_moderated', 'status']
    list_filter = ['created_at']
    search_fields = ['status', 'category']
    fields = ['title', 'description', 'image', 'price', 'category']
    readonly_fields = ['created_at', 'updated_at', 'public_at']


admin.site.register(Adverts, AdvertsAdmin)
admin.site.register(Status)
admin.site.register(Category)
