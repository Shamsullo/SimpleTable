from django.contrib import admin

from .models import SimpleTable


@admin.register(SimpleTable)
class SimpleTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'distance', 'time_stamp')
    list_display_links = ('name', 'time_stamp')
