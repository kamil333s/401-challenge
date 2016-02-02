from django.contrib import admin

from .models import Robot


class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'amount']

admin.site.register(Robot, ItemAdmin)
