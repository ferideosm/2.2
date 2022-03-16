from django.contrib import admin

from .models import Advertisement, Favorite

# Register your models here.

class FavoriteInline(admin.TabularInline):
    model = Favorite
    extra = 0

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    search_fields = ('id', 'title')
    list_display = ('id', 'title', 'description', 'status', 'creator', 'created_at', 'updated_at')
    list_display_links = ('id', 'title', 'description')
    inlines = [FavoriteInline]






    