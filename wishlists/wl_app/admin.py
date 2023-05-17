from django.contrib import admin

from .models import Wish, Gift


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    pass

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    pass
