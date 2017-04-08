from django.contrib import admin

from .models import Style


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    list_display = ('name', )