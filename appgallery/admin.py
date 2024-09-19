from django.contrib import admin

# Register your models here.

from .models import ArtItems,Category, Shop

admin.site.register(ArtItems)
admin.site.register(Shop)
admin.site.register(Category)