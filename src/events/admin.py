from django.contrib import admin

from .models import Event


@admin.register(Event)
class PubAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'description', 'place')
