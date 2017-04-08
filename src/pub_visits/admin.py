from django.contrib import admin

from .models import PubVisit

@admin.register(PubVisit)
class PubVisitAdmin(admin.ModelAdmin):
    list_display = ('date', )
